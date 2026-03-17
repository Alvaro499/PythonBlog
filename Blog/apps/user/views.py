from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render

# Views (they include POST, GET, DELETE...)
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from apps.user.forms import SignUpForm, LoginForm, UserForm, ProfileForm

from user.models import Profile

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


class UserUpdateView(LoginRequiredMixin, TemplateView):
    #if the person is not loggued, we kick them back to login
    login_url = 'login'
    #rebuilding the forms using the data send by user
    user_form = UserForm
    profile_form = ProfileForm

    def post(self, request):
        #Verify if a post request and a file were sent
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            #We apply changes
            user_form.save()
            profile_form.save()

            return redirect('index')

        # If there are errors, we show the page again using the same forms, so the correct data stays in the fields
        # and the errors are displayed.
        context = self.get_context_data(user_form=user_form, profile_form=profile_form)
        return render(request, context)

    def get(self, request, *args, **kwargs):
        if Profile.objects.filter(user=request.user).exists() == False:
            Profile.objects.create(user=request.user)
        return self.post(request, *args, **kwargs)

