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

]
