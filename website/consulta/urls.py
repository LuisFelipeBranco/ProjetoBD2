from django.urls import path
from .views import list_aluno, create_aluno, update_aluno, remove_aluno, index

urlpatterns = [
    path('', index, name='index'),
    path('createaluno/', create_aluno, name='create_aluno'),
    path('removealuno/', remove_aluno, name='create_aluno'),
    path('updatealuno/', update_aluno, name='create_aluno'),
    path('listaluno/', list_aluno, name='create_aluno'),
]