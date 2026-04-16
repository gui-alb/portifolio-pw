from django.shortcuts import render
from .models import Curso, Aluno, Professor


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