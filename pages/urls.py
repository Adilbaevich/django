from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('sale', sale, name='sale'),
    path('contact', contact, name='contact'),
    path('repairs', repairs, name='repairs'),
]