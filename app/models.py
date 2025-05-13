from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10, unique=True)

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Turma(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    ano = models.IntegerField()
    semestre = models.IntegerField()

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_matricula = models.DateField()

class Avaliacao(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    descricao = models.CharField(max_length=100)

class Historico(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota_final = models.DecimalField(max_digits=4, decimal_places=2)
    situacao = models.CharField(max_length=20)

