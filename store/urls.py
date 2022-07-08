from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('furniture/', furniture, name='furniture'),
    path('shop/', shop, name='shop'),
    path('testing/', testing, name='testing'),
    path('base/', base, name='base'),

    # AUTH
    path('login/', log_in, name='login'),
    path('register/', register, name='register'),
    path('log_out/', log_out, name='log_out'),
]
