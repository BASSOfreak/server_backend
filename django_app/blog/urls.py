from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('blog_entry/<int:pk>/', views.blog_entry, name='blog_entry'),
]