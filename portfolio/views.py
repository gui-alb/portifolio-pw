from django.shortcuts import render, redirect

from portfolio.models import Competencia, ContribuicaoOpenSource, Formacao, Licenciatura, Projeto, Tecnologia, TFC, UC

from .forms import *
import os
from django.conf import settings
# Create your views here.
def competencias_view(request):
    competencias = (Competencia.objects
              .select_related()
              .prefetch_related()
              .all())

    return render(request, 'portfolio/competencias.html', {'competencias': competencias})


def contribuicoesOpenSource_view(request):
    contribuicoes = (ContribuicaoOpenSource.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, 'portfolio/contribuicoes.html', {'contribuicoes': contribuicoes})


def formacoes_view(request):
    formacoes = (Formacao.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})


def licenciaturas_view(request):
    licenciaturas = (Licenciatura.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})


def projetos_view(request):
    projetos = (Projeto.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def tecnologias_view(request):
    tecnologias = (Tecnologia.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, 'portfolio/tecnologia.html', {'tecnologias': tecnologias})


def tfcs_view(request):
    tfcs = (TFC.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})


def unidadeCurricular_view(request):
    ucs = (UC.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, 'portfolio/unidadesCurriculares.html', {'ucs': ucs})

def novo_projeto_view(request):

    form = ProjetoForm()

    context = {'form': form}
    return render(request, 'portfolio/novo_projeto.html', context)

def editar_projeto_view(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.POST:
        form = ProjetoForm(request.POST or None, instance=projeto)

        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)

    context = {'form': form, 'projeto': projeto}

    return render(request, 'portfolio/edita_projeto.html', context)
def nova_tecnologia_view(request):

    form = TecnologiaForm()

    context = {'form': form}
    return render(request, 'portfolio/nova_tecnologia.html', context)

def nova_competencia_view(request):

    form = CompetenciaForm()

    context = {'form': form}
    return render(request, 'portfolio/nova_competencia.html', context)

def nova_formacao_view(request):

    form = FormacaoForm()

    context = {'form': form}
    return render(request, 'portfolio/nova_formacao.html', context)

def landing_page_view(request):

    path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'md')

    ficheiros = ['sobre.md', 'makingof.md']
    conteudos = {}

    for f in ficheiros:
        caminho = os.path.join(path, f)
        try:
            with open(caminho, 'r', encoding='utf-8') as file:
                conteudos[f] = file.read()
        except FileNotFoundError:
            conteudos[f] = None

    return render(request, 'portfolio/sobre.html', {
        'sobre_md': conteudos.get('sobre.md'),
        'makingof_md': conteudos.get('makingof.md'),
    })