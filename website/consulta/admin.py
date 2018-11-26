from django.contrib import admin
from .models import Aluno, Departamento, AlunosTurma, CadeirasCurso, Curso, Disciplina, Historico, Matricula, NotaAluno, Professor, SituacaoMatricula, TipoIngresso, Turma

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

class ProfessoresDisplay(admin.ModelAdmin):
    list_display = ('id', 'nome')

class AlunosTurmasDisplay(admin.ModelAdmin):
    list_display = ('id_matricula', 'turma_periodo')

class HistoricoDisplay(admin.ModelAdmin):
    list_display = ('id_matricula', 'id_disciplina')

class MatriculaDisplay(admin.ModelAdmin):
    list_display = ('id_aluno', 'id_curso')

class NotaAlunoDisplay(admin.ModelAdmin):
    list_display = ('id_matricula', 'nota1gq', 'nota2gq')

class HistoricoDisplay(admin.ModelAdmin):
    list_display = ('id_matricula', 'id_disciplina')

class CadeirasCursoDisplay(admin.ModelAdmin):
    list_display = ('id_curso', 'id_disciplina', 'obrigatoria')

admin.site.register(Aluno, AlunoDisplay)
admin.site.register(Departamento, DepartamentoDisplay)
admin.site.register(Curso, CursoDisplay)
admin.site.register(Disciplina, DisciplinaDisplay)
admin.site.register(Turma, TurmaDisplay)
admin.site.register(Professor, ProfessoresDisplay)
admin.site.register(AlunosTurma, AlunosTurmasDisplay)
admin.site.register(Matricula, MatriculaDisplay)
admin.site.register(NotaAluno, NotaAlunoDisplay)
admin.site.register(Historico, HistoricoDisplay)
admin.site.register(CadeirasCurso, CadeirasCursoDisplay)
admin.site.register(SituacaoMatricula)
admin.site.register(TipoIngresso)
