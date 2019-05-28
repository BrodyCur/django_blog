from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.shortcuts import render
from datetime import date
from blog.models import Article, Topic

def home_page(request):
  current_date = date.today()
  context = {
    'title': 'Django Blog',
    'date': current_date,
    'articles': Article.objects.filter(draft=False).order_by('-published_date')
    }
  response = render(request, 'index.html', context)
  return HttpResponse(response)

def article_page(request, id):
  article = Article.objects.get(pk=id)
  context = {
    'title': article.title,
    'article': article,
    }
  response = render(request, 'article.html', context)
  return HttpResponse(response)

def root(request):
  return HttpResponseRedirect('home/')