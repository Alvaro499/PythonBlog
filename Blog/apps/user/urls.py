from django.urls import path
from apps.user import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('add/', views.SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(http_method_names=['get', 'post']), name='logout'),
    path('edit/', views.UserUpdateView.as_view(), name='edit_user'),
    path('delete/', views.UserDeleteView.as_view(), name='delete_user')
]

