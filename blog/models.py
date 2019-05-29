from django.db import models


class Article(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField()
  draft = models.BooleanField()
  published_date = models.DateTimeField(auto_now_add=True)
  author = models.CharField(max_length=255)

  def __str__(self):
    return f'{self.title}'

class Topic(models.Model):
  category = models.CharField(max_length=255)
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='topic')

  def __str__(self):
    return f'{self.category}'

class Comment(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  message = models.TextField()
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')