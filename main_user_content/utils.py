from .models import *

top_menu = [{'title': 'Блог', 'menu_url': 'index'},
            {'title': 'О нас', 'menu_url': 'index'},
            {'title': 'Отзывы', 'menu_url': 'main_content_review'},
            {'title': 'Контакты', 'menu_url': 'contacts'}]


class HeaderMenuMixin:
    """
    Mixin with context for top menu and header.
    Included context:
    Telephone number,
    Top menu,
    all city's dropdown menu content
    all specializations for menu buttons with their names
    content_data_for_menu get all work types for default city in bd or selected city by slug
    """
    def get_menu_context(self, city_slug=None, **kwargs):
        telephone = TelephoneNumber.objects.all()
        telephone_href = self.telephone_href(telephone)
        telephone_view = self.telephone_view(telephone)
        context = kwargs
        default_city = City.objects.filter(is_default=True)    # pointed default city in table city
        if not city_slug and len(default_city) > 0:            # check url slug or pointed default city -
            city_slug = default_city[0].slug                   # - for header menu
        content_data_for_menu = MainUserContent.objects.filter(city__slug=city_slug).order_by(
                                                                                            'work_type__work_type_name'
                                                                                                )
        # content_data_for_menu get list of works or empty result for menu

        all_specializations = Specialization.objects.all()
        all_cityes = City.objects.all()
        context['telephone_href'] = telephone_href
        context['telephone_view'] = telephone_view
        context['content_data_for_menu'] = content_data_for_menu
        context['all_specializations'] = all_specializations
        context['all_cityes'] = all_cityes
        context['top_menu'] = top_menu
        return context

    @staticmethod
    def telephone_href(tel_qs):
        """
        Make a telephone link for calling
        """
        if len(tel_qs) > 0:
            tel = tel_qs[0].telephone_number
            return f'tel:+7{tel[1:]}'
        return '#'

    @staticmethod
    def telephone_view(tel_qs):
        """
        Make a telephone number view
        """
        if len(tel_qs) > 0:
            tel = tel_qs[0].telephone_number
            return f'8 ({tel[1:4]}) {tel[4:7]} {tel[7:9]} {tel[9:]}'
        return 'Добавьте номер в ЛК'
