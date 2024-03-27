from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import choice
from ..scripts.date import den_name
from ..models import *

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


def adress_view(request, city, street):
    # http://127.0.0.1:8000/country/hlavni/0
    cities = {"hlavni": "Praha",
              "mensi": "Brno"}

    streets = ["prvni", "druha", "treti"]

    my_city = cities.get(city)
    my_street = streets[street]

    template = loader.get_template('adress.html')
    context = {
        'city_name': my_city,
        "street": my_street
    }
    return HttpResponse(template.render(context, request))



def adress_view2(request):
    # http://127.0.0.1:8000/country/?city=hlavni&street=0
    cities = {"hlavni": "Praha",
              "mensi": "Brno"}

    streets = ["prvni", "druha", "treti"]

    my_city = cities.get(request.GET["city"])
    my_street = streets[int(request.GET["street"])]

    template = loader.get_template('adress.html')
    context = {
        'city_name': my_city,
        "street": my_street
    }
    return HttpResponse(template.render(context, request))