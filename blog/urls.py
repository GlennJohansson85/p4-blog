from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete/', views.delete_post_confirmation, name='delete_post_confirmation'),
    path('post/<int:post_id>/delete/confirm/', views.delete_post, name='delete_post'),
]
