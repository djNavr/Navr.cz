from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import choice
from .scripts.date import den_name
from .models import *

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

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def phones(request):
  phones = Phones.objects.all().values()
  template = loader.get_template('phones.html')
  context = {
    'phones': phones,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))