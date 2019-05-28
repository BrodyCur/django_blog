from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.shortcuts import render
from datetime import date
from blog.models import Article, Topic

def home_page(request):
  current_date = date.today()
  context = {
    'date': current_date,
    'articles': Article.objects.all()
    }
  response = render(request, 'index.html', context)
  return HttpResponse(response)

def article_page(request, id):
  article = Article.objects.get(pk=id)
  context = {
    'article': article,
    }
  response = render(request, 'article.html', context)
  return HttpResponse(response)

def root(request):
  return HttpResponseRedirect('home/')