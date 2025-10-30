from django.urls import path 
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    #login
    path('login/',login_view,name='login'),
    #logout
    path('logout/',logout_view,name='logout'),
    #signup
    path('signup/',signup_view,name='signup'),
    #password reset process
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]