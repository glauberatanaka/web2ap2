from django.db import models

class Curso(models.Model):
    curso_nome = models.CharField(max_length=100, unique=True)
    bloco = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.curso_nome

class Aluno(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="curso")
    nome = models.CharField(max_length=256)
    idade = models.IntegerField()
    semestre = models.IntegerField()
    rga = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.nome