from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Views (they include POST, GET, DELETE...)
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from apps.user.forms import SignUpForm, LoginForm

#Overrida tag
from typing import override


class SignUpView(CreateView):

    form_class = SignUpForm
    template_name = 'login/register.html'
    success_url = reverse_lazy('index')

    @override
    def form_valid(self, form):
        form.save()

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )

        login(self.request, user)
        return redirect('index')

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login/login.html'
