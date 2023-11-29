from django.shortcuts import render, HttpResponse


# Create your views here.

def article_list(request):
    return HttpResponse(" This is changed now. urls.py in article folder")
