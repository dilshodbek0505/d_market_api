from django.urls import path

from .api_endpoints import *

app_name = 'user'

urlpatterns = [
    # user auth
    path('login/', LoginApi.as_view(), name='user-login'),
    path('register/', RegisterApi.as_view(), name='user-register'),
    path('otp/', PhoneNumberOtpApi.as_view(), name='user-otp'),
    # user details
    path('details/', UserRetrieveUpdateApi.as_view(), name='user-details')

]
