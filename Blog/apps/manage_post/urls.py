from django.urls import path
from apps.manage_post import views

urlpatterns = [
    path('', views.index, name='index')
]
