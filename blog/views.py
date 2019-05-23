from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import date

def home_page(request):
  current_date = date.today()
  context = {
    'date': current_date,
    }
  response = render(request, 'index.html', context)
  return HttpResponse(response)

def root(request):
  return HttpResponseRedirect('home/')