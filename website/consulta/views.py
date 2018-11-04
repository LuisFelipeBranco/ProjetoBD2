from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import aluno, departamento, tipo_ingresso


def index(request):
    return HttpResponse("<h1>As consultas do banco ficaram aqui!</h1>")

def create_aluno(request):
    return HttpResponse("<h1>As consultas do banco ficaram aqui!</h1>")

def remove_aluno(request):
    return HttpResponse("<h1>As consultas do banco ficaram aqui!</h1>")

def update_aluno(request):
    return HttpResponse("<h1>As consultas do banco ficaram aqui!</h1>")

def list_aluno(request):
    student = aluno.objects.all()
    return render(request, 'student.html', {'student':student})