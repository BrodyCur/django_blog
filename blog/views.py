from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.shortcuts import render, redirect
from datetime import date
from blog.models import Article, Topic, Comment
from django.views.decorators.http import require_http_methods

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
  return HttpResponseRedirect('home')

@require_http_methods(['POST'])
def create_comment(request):
  article_id = request.POST['article']
  article = Article.objects.get(id=article_id)
  comment_name = request.POST['name']
  comment_msg = request.POST['message']
  Comment.objects.create(name=comment_name , message=comment_msg , article=article)
  return redirect('article_details', id=article.id)