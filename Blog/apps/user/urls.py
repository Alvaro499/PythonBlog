from django.urls import path
from apps.user import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('add/', views.SignUpView.as_view(), name='register')
]
