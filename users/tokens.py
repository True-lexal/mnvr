from django.contrib.auth.tokens import PasswordResetTokenGenerator


class EmailConfirmTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        """
        Make hash for token to activate by checking 'is_confirmed' field
        """
        return f"{user.pk}{user.is_confirmed}{timestamp}{user.email}"


email_confirm_token_generator = EmailConfirmTokenGenerator()
