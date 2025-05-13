from django.contrib import admin
from .models import Curso, Disciplina, Professor, Aluno, Turma, Matricula, Avaliacao, Historico

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Historico)

