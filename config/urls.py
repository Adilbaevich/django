from django.contrib import admin
from django.urls import path
from pages.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about', about, name='about'),
    path('sale', sale, name='sale'),
    path('contact', contact, name='contact'),
    path('repairs', repairs, name='repairs'),
]