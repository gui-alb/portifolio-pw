from django.shortcuts import render, get_object_or_404
from .models import *


def cursos_view(request):
    cursos = (Curso.objects
              .select_related()
              .prefetch_related()
              .all())

    return render(request, 'escola/cursos.html', {'cursos': cursos})

def professores_view(request):
    professores = (Professor.objects
                   .select_related()
                   .prefetch_related()
                   .all)

    return render(request, 'escola/professores.html', {'professores': professores})

def alunos_view(request):
    alunos = (Aluno.objects
                   .select_related()
                   .prefetch_related()
                   .all())

    return render(request, 'escola/alunos.html', {'alunos': alunos})

def curso_view(request, id):
    curso = (Curso.objects.get(id=id))
    return render(request, 'escola/curso.html', {'curso': curso})