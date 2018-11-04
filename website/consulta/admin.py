from django.contrib import admin
from .models import aluno, departamento, curso

admin.site.register(aluno)
admin.site.register(departamento)
admin.site.register(curso)