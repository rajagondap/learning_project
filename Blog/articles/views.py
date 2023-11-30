from django.shortcuts import render, HttpResponse
from .models import Article


# Create your views here.

def article_list(request):
    article_list = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'article_list': article_list})
