from django.urls import path
from apps.user import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('add/', views.SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]

