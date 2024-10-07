from django.urls import path

from . import views

app_name = 'match'

urlpatterns = [
    path('', views.index),
    path('<int:match_id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('join/<int:match_id>', views.join, name='join'),
    path('leave/<int:match_id>', views.leave, name='leave'),
]