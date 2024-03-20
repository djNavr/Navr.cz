from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import choice
from .scripts.date import den_name

def home_page(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def news(request):
  template = loader.get_template('news.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  sentence = choice(['jedna','dva','tri'])
  den = den_name()
  context = {
    'sentence' : sentence,
    'den' : den,
  }
  return HttpResponse(template.render(context, request))

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())