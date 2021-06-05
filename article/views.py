import django
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, FormView, RedirectView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Article, UserFavouriteArticle
from .forms import ArticleForm

# Create your views here.
class ArticleView(ListView):
    model = Article
    template_name = 'article.html'

class HomeView(RedirectView):
    pattern_name = 'article'

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Publications(FormView):
    form_class = ArticleForm
    template_name = 'publish.html'
    success_url = '/'
    def form_valid(self, form:ArticleForm):
        # post = form(self.request.POST)
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Invalid information.")
        return super().form_invalid(form)
