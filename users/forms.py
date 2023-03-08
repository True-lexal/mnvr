from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUsers


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUsers
        fields = ('username', 'email', 'password1', 'password2')
