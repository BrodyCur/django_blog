from django import forms
from blog.models import Comment, Article
from django.utils import timezone

class ArticleForm(forms.ModelForm):
  published_date = forms.DateTimeField(widget=forms.SelectDateWidget())
  class Meta:
    model = Article
    fields = ('title', 'body', 'draft', 'author', 'published_date')

  def clean(self):
    data = super().clean()
    body = data.get('body')
    if len(body) <= 1:
      self.add_error('body', 'Body must be longer than 1 character.')
    draft = data.get('draft')
    published_date = data.get('published_date')
    present = timezone.now()
    if draft == True and published_date < present:
      self.add_error('published_date', 'Publishing date must be in the future.')
    elif draft == False and published_date > present:
      self.add_error('published_date', 'Publishing date must be in the past.')