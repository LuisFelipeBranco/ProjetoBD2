from django.contrib import admin
from .models import Aluno, Departamento, AlunosTurma, CadeirasCurso, Curso, Disciplina, Historico, Matricula, NotaAluno,Professor, SituacaoMatricula, TipoIngresso, Turma
admin.site.register(Aluno)
admin.site.register(Departamento)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Turma)