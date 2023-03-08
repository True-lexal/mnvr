from django.contrib import admin

from .models import *


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialization_name', 'slug')
    list_display_links = ('id', 'specialization_name')
    prepopulated_fields = {'slug': ('specialization_name',)}


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'is_default', 'slug')
    list_display_links = ('id', 'city_name')
    list_editable = ('is_default',)
    prepopulated_fields = {'slug': ('city_name',)}


class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'work_type_name', 'slug')
    list_display_links = ('id', 'work_type_name')
    prepopulated_fields = {'slug': ('work_type_name',)}


class MainUserContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'work_type', 'specialization', 'city')
    list_filter = ('specialization', 'city')
    search_fields = ('work_type',)
    list_display_links = ('id', 'work_type')


class MainContentReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'review_author', 'review_content', 'is_published', 'city', 'specialization', 'work_type')
    search_fields = ('review_content', 'work_type')
    list_filter = ('city', 'specialization')
    list_display_links = ('id', 'review_content')
    list_editable = ('is_published', 'work_type')


class MainContentReviewAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'review_author', 'answer_content')
    search_fields = ('answer_content',)
    list_filter = ('review',)
    list_display_links = ('id', 'answer_content')


admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(MainUserContent, MainUserContentAdmin)
admin.site.register(MainContentReview, MainContentReviewAdmin)
admin.site.register(MainContentReviewAnswer, MainContentReviewAnswerAdmin)
admin.site.register(TelephoneNumber)
