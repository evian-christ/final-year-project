from django.urls import path

from . import views

app_name = 'notifc'

urlpatterns = [
    path('', views.index, name='index'),
]