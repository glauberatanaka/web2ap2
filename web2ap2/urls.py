"""web2ap2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from alunosApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alunos/', include('alunosApp.urls')),
    path('admin/', admin.site.urls),
    path('adicionar/curso', views.form_curso, name='form_curso'),
    path('adicionar/aluno', views.form_aluno, name='form_aluno')

]
