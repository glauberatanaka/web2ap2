from django import forms
from alunosApp.models import Curso, Aluno

class FormCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
    # curso_nome = forms.CharField(label='Nome', max_length=100)
    # bloco = forms.CharField(label='Bloco', max_length=100)

class FormAluno(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
    # curso = forms.ModelChoiceField(queryset = Curso.objects.all())
    # nome = forms.CharField(label='Nome', max_length=256)
    # idade = forms.IntegerField(label='Idade')
    # semestre = forms.IntegerField(label='Semestre')
    # rga = forms.CharField(label='RGA', max_length=12)