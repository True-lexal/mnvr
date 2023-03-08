from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.views.generic.edit import ModelFormMixin, FormMixin, BaseCreateView, ProcessFormView

from .models import *
from .utils import HeaderMenuMixin
from .forms import *


class Index(HeaderMenuMixin, TemplateView):
    """
    Render a template of main page
    """
    template_name = 'main_user_content/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_menu_context(title='Главная страница')
        return {**context, **add_context}


class MainContentText(HeaderMenuMixin, DetailView):
    """
    Remder a template with main content of service
    Added reviews filtered by current work type
    """
    template_name = 'main_user_content/main_content.html'
    context_object_name = 'main_content'
    slug_url_kwarg = 'work_slug'
    slug_field = 'work_type__slug'

    def get_queryset(self):
        return MainUserContent.objects.filter(city__slug=self.kwargs['city_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        work_type_review = MainContentReview.objects.filter(city=context['main_content'].city,
                                                            specialization=context['main_content'].specialization,
                                                            work_type=context['main_content'].work_type)
        add_context = self.get_menu_context(city_slug=self.kwargs['city_slug'],
                                            title=context['main_content'].title,
                                            work_type_review=work_type_review
                                            )
        return {**context, **add_context}


class CityContent(HeaderMenuMixin, ListView):
    """
    Render a template with list of services filtered by selected city ordered by work type name
    """
    template_name = 'main_user_content/list_content.html'
    context_object_name = 'city_content'
    allow_empty = False

    def get_queryset(self):
        return MainUserContent.objects.filter(city__slug=self.kwargs['city_slug']).order_by('work_type__work_type_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = context['city_content'][0].city
        add_context = self.get_menu_context(city_slug=self.kwargs['city_slug'], title=title)
        return {**context, **add_context}


class MainContentReviewShow(HeaderMenuMixin, ListView):
    """
    Show all reviews
    Add a form for adding review answer
    """
    queryset = MainContentReview.objects.filter(is_published=True).order_by('-time_create')
    template_name = 'main_user_content/main_content_review_show.html'
    context_object_name = 'all_reviews'
    form = ReviewAnswerFormContent()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answer_review = MainContentReviewAnswer.objects.all()
        add_context = self.get_menu_context(title='Отзывы', answer_review=answer_review, form=self.form)
        return {**context, **add_context}


class MainContentReviewAdd(HeaderMenuMixin, CreateView):
    """
    Add new review view
    """
    form_class = ReviewForm
    template_name = 'main_user_content/main_content_review_add.html'
    success_url = reverse_lazy('main_content_review')

    def get_form_kwargs(self):
        """Add current logged-in user or none in form kwargs"""
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'current_user': self.request.user if self.request.user.is_authenticated else None,
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_menu_context(title='Добавить отзыв')
        return {**context, **add_context}


def review_answer_add(request, review_pk):
    """
    Add parent review id and review author to user form
    Add review answer corrected form from user to bd
    """
    if request.method == 'POST':
        form = ReviewAnswerForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.review_id = review_pk
            obj.review_author = request.user
            obj.save()
    return redirect('main_content_review')


def contacts_page(request):
    return render(request, 'main_user_content/index.html')
