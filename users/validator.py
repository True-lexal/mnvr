from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UnicodeUsernameValidatorNew(validators.RegexValidator):
    """
    Validator of username with allowed simbols:
    a-z, A-Z, -
    """
    regex = r"^[\w-]+\Z"
    message = "Допустимы только цифры, латинские буквы и символ '-' !"
    flags = 0
