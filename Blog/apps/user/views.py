from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.user.forms import SignUpForm

class SignUpView(CreateView):

    form_class = SignUpForm
    template_name = 'login/register.html'
    success_url = reverse_lazy('index')

def login(request):
    return HttpResponse("Hello World")