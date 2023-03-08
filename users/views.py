from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, TemplateView, PasswordResetView, PasswordResetDoneView, \
                                        PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .tokens import email_confirm_token_generator
from .utils import TopMenuMixin, send_confirm_email


class Register(TopMenuMixin, CreateView):
    """
    Render a template with register form
    and after registration send email to registered user with token link for activation
    """
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('confirm_email')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_top_menu_context(title='Регистрация')
        return {**context, **add_context}

    def get_success_url(self):
        """
        After registration make token and send email to user
        amd then go to success url
        """
        send_confirm_email(self.object, self.request)
        return str(self.success_url)


class Login(TopMenuMixin, LoginView):
    """
    Render a login template with login form
    """
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_top_menu_context(title='Авторизация')
        return {**context, **add_context}

    def get_success_url(self):
        return reverse_lazy('lk')


class MainLk(LoginRequiredMixin, TopMenuMixin, TemplateView):
    """
    Render a template of personal area only to log in user
    """
    template_name = 'users/main_lk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_top_menu_context(title='Личный кабинет')
        return {**context, **add_context}


def logout_user(request):
    logout(request)
    return redirect('index')


class CustomPasswordResetView(TopMenuMixin, PasswordResetView):
    """
    Render a template with email form and send email with token link
    """
    template_name = 'users/recover/password_reset_form.html'
    email_template_name = 'users/recover/password_reset_email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_top_menu_context()
        return {**context, **add_context}


class CustomPasswordResetDoneView(TopMenuMixin, PasswordResetDoneView):
    """
    Check token and render a template with result
    """
    template_name = 'users/recover/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_top_menu_context()
        return {**context, **add_context}


class CustomPasswordResetConfirmView(TopMenuMixin, PasswordResetConfirmView):
    """
    Check token and render a template with password change forms
    """
    template_name = 'users/recover/password_reset_confirm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_top_menu_context()
        return {**context, **add_context}


class CustomPasswordResetCompleteView(TopMenuMixin, PasswordResetCompleteView):
    """
    Render a template after successful changing a password
    """
    template_name = 'users/recover/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_top_menu_context()
        return {**context, **add_context}


class ConfirmEmail(TopMenuMixin, TemplateView):
    """
    Render a template after registration
    """
    template_name = 'users/confirm_email/confirm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_top_menu_context(title='Регистрация успешна')
        return {**context, **add_context}


class ActivateEmail(TopMenuMixin, TemplateView):
    """
    Confirming email by link from users email
    and render result
    """
    template_name = 'users/confirm_email/activate.html'

    @staticmethod
    def activate(uidb64, token):
        """
        Check token. If valid make email confirmed. Return result string for context.
        """
        User = get_user_model()
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and email_confirm_token_generator.check_token(user, token):
            user.is_confirmed = True
            user.save()
            return 'Ваш Email успешно подтвержден. Аккаунт активирован!'
        else:
            return 'Не существующая ссылка активации!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        result_message = self.activate(uidb64, token)
        add_context = self.get_top_menu_context(title='Подтверждение...', result_message=result_message)
        return {**context, **add_context}
