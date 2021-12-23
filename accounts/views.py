from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.contrib.auth import mixins
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Register(generic.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse("blog:home")


class LoginUser(LoginView):
    template_name = 'accounts/login.html'


class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'


class AccountHome(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/home.html'
    model = User
