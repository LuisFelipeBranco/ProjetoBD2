from django.contrib import admin
from .models import Aluno, Departamento, AlunosTurma, CadeirasCurso, Curso, Disciplina, Historico, Matricula, NotaAluno,Professor, SituacaoMatricula, TipoIngresso, Turma

class AlunoDisplay(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    search_fields = ('id', 'nome')

class DepartamentoDisplay(admin.ModelAdmin):
    list_display = ('id', 'nome', 'bloco')

class CursoDisplay(admin.ModelAdmin):
    list_display = ('id', 'nome')

class DisciplinaDisplay(admin.ModelAdmin):
    list_display = ('id', 'nome')

class TurmaDisplay(admin.ModelAdmin):
    list_display = ('nome', 'periodo')

class ProfessorDisplay(admin.ModelAdmin):
    list_display = ('id', 'nome')

class AlunosTurmasDisplay(admin.ModelAdmin):
    list_display = ('id_matricula', 'turma_disciplina')

class HistoricoDisplay(admin.ModelAdmin):
    list_display = ('id_matricula', 'id_disciplina')

admin.site.register(Aluno, AlunoDisplay)
admin.site.register(Departamento, DepartamentoDisplay)
admin.site.register(Curso, CursoDisplay)
admin.site.register(Disciplina, DisciplinaDisplay)
admin.site.register(Turma, TurmaDisplay)
admin.site.register(Professor, ProfessorDisplay)
admin.site.register(AlunosTurma)
admin.site.register(Historico)
admin.site.register(CadeirasCurso)