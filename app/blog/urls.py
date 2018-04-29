from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog'),
    path('<int:post_id>/', views.post, name='post'),
    path('slug/<str:slug>/', views.slug, name='slug')
]
