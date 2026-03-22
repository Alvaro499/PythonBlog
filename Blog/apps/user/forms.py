# we import every django form methods
from django import forms

#it contains all django logic forms (passwords, errors, validations)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from django.contrib.auth import get_user_model
from apps.user.models import Profile

User = get_user_model()

class SignUpForm(UserCreationForm):

    username = forms.CharField(help_text='',
                               label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    full_name = forms.CharField(help_text='',
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
                               help_text='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'})
                               )
    password = forms.CharField(label=False,
                               help_text='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
                               )
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class UserForm(forms.ModelForm):

    username = forms.CharField(help_text='',
                               label='Username')
    full_name = forms.CharField(help_text='',
                                label='Full Name')
    email = forms.EmailField(help_text='',
                             label='New Email')


    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
        ]


class ProfileForm(forms.ModelForm):

    photo = forms.ImageField(label="Photo",
                             help_text='',
                             required=False,
                             widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = [
            'photo',
            'profession',
            'about',
            'birthday',
            'twitter',
            'linkedin',
            'facebook'
        ]

class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]
