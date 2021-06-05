from django.forms import ModelForm
from .models import Article

# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']
