from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('about', views.about_page, name='about'),
    path('about_post/<int:pk>/', views.about_post_detail, name='about_post_detail'),
    path('about_post/<int:pk>/edit', views.about_post_edit, name='about_post_edit'),
] 
