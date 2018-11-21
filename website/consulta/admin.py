from django.contrib import admin
from .models import Aluno, Departamento, AlunosTurma, CadeirasCurso, Curso, Disciplina, Historico, Matricula, NotaAluno,Professor, SituacaoMatricula, TipoIngresso, Turma


class AlunoDisplay(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    search_fields = ('id', 'nome')

class DepartamentoDisplay(admin.ModelAdmin):
    list_display = ('id', 'nome', 'bloco')

admin.site.register(Aluno, AlunoDisplay)
admin.site.register(Departamento, DepartamentoDisplay)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Turma)