from django.contrib.auth.backends import ModelBackend, UserModel


class NameEmailAuthBackend(ModelBackend):
    """
    Make username or email available in same field in log in
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if '@' in username:
            enter_login = {'email': username}
        else:
            enter_login = {'username': username}
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get(**enter_login)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
