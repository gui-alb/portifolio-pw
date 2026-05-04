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

    form = ProjetoForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('projetos')

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

def apagar_projeto(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')

    return render(request, 'portfolio/delete_projeto.html', {'projeto': projeto})

def nova_tecnologia_view(request):

    form = TecnologiaForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('tecnologias')

    context = {'form': form}
    return render(request, 'portfolio/nova_tecnologia.html', context)

def editar_tecnologia_view(request, id):
    tecnologia = Tecnologia.objects.get(id=id)

    if request.POST:
        form = TecnologiaForm(request.POST or None, instance=tecnologia)

        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)

    context = {'form': form, 'projeto': tecnologia}

    return render(request, 'portfolio/edita_tecnologia.html', context)

def apagar_tecnologia_view(request, id):
    tecnologia = Tecnologia.objects.get(id=id)

    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')

    return render(request, 'portfolio/delete_tecnologia.html', {'tecnologia': tecnologia})

def nova_competencia_view(request):

    form = CompetenciaForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('competencias')

    context = {'form': form}
    return render(request, 'portfolio/nova_competencia.html', context)


def editar_competencia_view(request, id):
    competencia = Competencia.objects.get(id=id)

    if request.POST:
        form = CompetenciaForm(request.POST or None, instance=competencia)

        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)

    return render(request, 'portfolio/edita_competencia.html', {'form': form, 'competencia': competencia})

def apagar_competencia_view(request, id):
    competencia = Competencia.objects.get(id=id)

    if request.POST:
        competencia.delete()
        return redirect('competencias')

    return render(request, 'portfolio/delete_competencia.html', {'competencia': competencia})
def nova_formacao_view(request):
    form = FormacaoForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('formacoes')

    context = {'form': form}
    return render(request, 'portfolio/nova_formacao.html', context)


def editar_formacao_view(request, id):
    formacao = Formacao.objects.get(id=id)

    if request.POST:
        form = FormacaoForm(request.POST or None, instance=formacao)

        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)

    return render(request, 'portfolio/edita_formacao.html', {'form': form, 'formacao': formacao})

def apagar_formacao_view(request, id):
    formacao = Formacao.objects.get(id=id)

    if request.POST:
        formacao.delete()
        return redirect('formacoes')

    return render(request, 'portfolio/delete_formacao.html', {'formacao': formacao})

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