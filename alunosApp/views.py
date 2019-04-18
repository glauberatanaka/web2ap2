from django.shortcuts import render
from django.http import HttpResponse
from alunosApp.models import Curso, Aluno
from . import forms
# Create your views here.

def index(request):
    alunos_list = Aluno.objects.order_by('nome')
    alunos_dict = {'alunos': alunos_list}
    return render(request, 'alunosApp/index.html', context=alunos_dict)

def form_curso(request):
    form = forms.FormCurso()

    if request.method == 'POST':
        form = forms.FormCurso(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
    return render(request, 'alunosApp/form_curso.html', {'form':form})

def form_aluno(request):
    form = forms.FormAluno()

    if request.method == 'POST':
        form = forms.FormAluno(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
    return render(request, 'alunosApp/form_aluno.html', {'form':form})