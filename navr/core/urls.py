from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name="Home page"),
    path('news', news, name="News page"),
    path('contact', contact, name="Contact page"),
    path('about', about, name="About page"),
    path('members', members, name="members"),
    path('phones', phones, name="phones"),
]