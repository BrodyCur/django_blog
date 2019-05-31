from django.contrib import admin
from blog.models import Article, Topic, Comment

admin.site.register(Article)
admin.site.register(Topic)
admin.site.register(Comment)