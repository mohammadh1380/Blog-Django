from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.contrib.auth import mixins
from .forms import RegisterForm


# Create your views here.

class Register(generic.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse("blog:home")
