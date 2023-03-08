from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.core.exceptions import ValidationError
from users.models import CustomUsers


class Specialization(models.Model):
    specialization_name = models.CharField(max_length=100, db_index=True, verbose_name='Специализация')
    slug = models.SlugField(max_length=80, unique=True, db_index=True, verbose_name='url slug')

    def __str__(self):
        return self.specialization_name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class City(models.Model):
    city_name = models.CharField(max_length=200, db_index=True, verbose_name='Город')
    slug = models.SlugField(max_length=80, unique=True, db_index=True, verbose_name='url slug')
    is_default = models.BooleanField(verbose_name='услуги по выбранному городу отображаются в меню по умолчанию (1шт.)',
                                     default=False)

    def __str__(self):
        return self.city_name

    def get_absolute_url(self):
        return reverse('city_content', kwargs={'city_slug': self.slug})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class WorkType(models.Model):
    """
    Type of work
    One for each service
    """
    work_type_name = models.CharField(max_length=255, db_index=True, verbose_name='Вид работы')
    slug = models.SlugField(max_length=80, db_index=True, verbose_name='url slug')

    def __str__(self):
        return self.work_type_name

    class Meta:
        verbose_name = 'Тип работ'
        verbose_name_plural = 'Тип работы'


class MainUserContent(models.Model):
    """
    Main text and photo content
    preview_img is small img for preview in the list of services by city or etc
    """
    preview_img = models.ImageField(upload_to="type-preview/%Y/%m/%d/",
                                    verbose_name='Картинка превью в списке услуг', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='title страницы')
    h1 = models.CharField(max_length=100, verbose_name='Тэг H1')
    main_content = RichTextUploadingField(verbose_name='Основной сео контент')
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, verbose_name='Специализация')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    work_type = models.ForeignKey(WorkType, on_delete=models.PROTECT, verbose_name='Вид работы')

    def __str__(self):
        return self.work_type.work_type_name

    def get_absolute_url(self):
        return reverse('main_content_text', kwargs={'work_slug': self.work_type.slug,
                                                    'city_slug': self.city.slug,
                                                    'specialization_slug': self.specialization.slug
                                                    })

    class Meta:
        verbose_name = 'Основной пользовательский контент'
        verbose_name_plural = 'Основной пользовательский контент'


class BaseReview(models.Model):
    """
    Abstract class for reviews classes
    """
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')
    review_author = models.ForeignKey(CustomUsers, on_delete=models.PROTECT, null=True,
                                      blank=True, verbose_name='Автор')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        abstract = True


class MainContentReview(BaseReview):
    review_content = models.TextField(verbose_name='Отзыв')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, verbose_name='Специализация')
    work_type = models.ForeignKey(WorkType, on_delete=models.PROTECT, verbose_name='Вид работ', null=True, blank=True)

    def __str__(self):
        return self.review_content[:25]

    class Meta:
        verbose_name = 'Отзыв услуг'
        verbose_name_plural = 'Отзывы услуг'


class MainContentReviewAnswer(BaseReview):
    answer_content = models.TextField(verbose_name='Ответ')
    review = models.ForeignKey(MainContentReview, on_delete=models.CASCADE, verbose_name='Отзыв', blank=True, null=True)

    def __str__(self):
        return self.answer_content[:25]

    class Meta:
        verbose_name = 'Ответ на отзывы усл.'
        verbose_name_plural = 'Ответы на отзывы усл.'


def telephone_validator(value):
    """check telephone number be like 89991234567"""
    if not value.isdigit():
        raise ValidationError('Вводите только цифры')
    if len(value) != 11:
        raise ValidationError(f'Должно быть 11 цифр, а не {len(value)}')
    if value[0] != '8':
        raise ValidationError(f'Номер должен начинаться с 8, а не с {value[0]}')
    else:
        return value


class TelephoneNumber(models.Model):
    """
    Telephone number for incoming calls
    """
    telephone_number = models.CharField(max_length=11, validators=(telephone_validator,),
                                        verbose_name='Номер телефона начиная с 8 без пробелов и скобок, только цифры')

    def __str__(self):
        return self.telephone_number

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'
