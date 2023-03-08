from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('password-recovery/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-recovery-ok/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-recovery-conf/<slug:uidb64>/<slug:token>/',
         CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-recovery-complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('confirm/', ConfirmEmail.as_view(), name='confirm_email'),
    path('activate/<slug:uidb64>/<slug:token>/',
         ActivateEmail.as_view(),
         name='activate_email'),
    path('activate/', ActivateEmail.as_view(), name='activate'),
    path('', MainLk.as_view(), name='lk'),

]
