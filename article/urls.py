from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/', views.ArticleView.as_view(), name='article'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('resister/', views.SignUp.as_view(), name='signup'),
    path('publish/', login_required(views.Publications.as_view()), name='publish'),
]
