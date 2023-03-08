
from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contacts/', contacts_page, name='contacts'),
    path('reviews/add-review/', MainContentReviewAdd.as_view(), name='main_content_review_add'),
    path('reviews/add-answer/<int:review_pk>/', review_answer_add, name='review_answer_add'),
    path('reviews/', MainContentReviewShow.as_view(), name='main_content_review'),
    path('<slug:city_slug>/', CityContent.as_view(), name='city_content'),
    path('<slug:city_slug>/<slug:specialization_slug>/<slug:work_slug>/',
         MainContentText.as_view(), name='main_content_text'),
]
