from django.shortcuts import render
from django.http import HttpResponse
from alunosApp.models import Curso, Aluno
# Create your views here.

def index(request):
    alunos_list = Aluno.objects.order_by('nome')
    alunos_dict = {'alunos': alunos_list}
    return render(request, 'alunosApp/index.html', context=alunos_dict)