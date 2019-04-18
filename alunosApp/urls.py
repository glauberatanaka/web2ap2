from django.urls import path
from alunosApp import views

urlpatterns = [
    path('', views.index, name='index'),
]