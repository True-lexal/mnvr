from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from mnvr.settings import DEFAULT_FROM_EMAIL
from .tokens import email_confirm_token_generator


top_menu = [{'title': 'Блог', 'menu_url': 'index'},
            {'title': 'Главная', 'menu_url': 'index'},
            {'title': 'Отзывы', 'menu_url': 'main_content_review'},
            {'title': 'Контакты', 'menu_url': 'contacts'}]


class TopMenuMixin:
    """
    Mixin for top menu
    """
    def get_top_menu_context(self, **kwargs):
        context = kwargs
        context['top_menu'] = top_menu
        return context


def send_confirm_email(obj, request,  use_https=False):
    """Send email with token link to new user"""

    usermodel = get_user_model()  # get usermodel pointed in settings
    token_generator = email_confirm_token_generator
    current_site = get_current_site(request)
    site_name = current_site.name
    domain = current_site.domain
    username = obj.username
    user_email_to = obj.email
    users = usermodel.objects.filter(username=username, email=user_email_to)
    email_template_name = 'users/confirm_email/send_confirm_email.html'
    subject = f'Регистрация на {site_name}'
    from_email = DEFAULT_FROM_EMAIL
    for user in users:
        context = {
            "email": user_email_to,
            "domain": domain,
            "site_name": site_name,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "user": user,
            "token": token_generator.make_token(user),
            "protocol": "https" if use_https else "http",
        }
        body = loader.render_to_string(email_template_name, context)
        sending_email = EmailMultiAlternatives(subject, body, from_email, [user_email_to])
        sending_email.send()
