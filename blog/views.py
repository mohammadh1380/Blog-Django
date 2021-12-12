from django.shortcuts import render
from django.views import generic
from .models import Article


# Create your views here.

class HomeView(generic.ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    ordering = ['publish']
