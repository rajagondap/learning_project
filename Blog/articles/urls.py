
from django.urls import path
from .views import article_list, article_details, user_login, register

urlpatterns = [
    path('', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
]
