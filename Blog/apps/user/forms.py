# we import every django form methods
from django import forms

#it contains all django logic forms (passwords, errors, validations)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):

    username = forms.CharField(help_text=None,
                               label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    full_name = forms.CharField(help_text=None,
                               label=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(label=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = [
            "username",
            "full_name",
            "email",
            "password1",
            "password2",
        ]

class LoginForm(AuthenticationForm):

    username = forms.CharField(label=False,
                               help_text=None,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'})
                               )
    password = forms.CharField(label=False,
                               help_text=None,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
                               )
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
