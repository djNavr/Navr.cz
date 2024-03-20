from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name="Home page"),
    path('news', news, name="News page"),
    path('contact', contact, name="Contact page"),
    path('about', about, name="About page"),
    path('phones', phones, name="phones"),
    path('details', details, name="details"),
    path('members', members, name='members'),
    path('details/<int:id>', details, name='details'),

]