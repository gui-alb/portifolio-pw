from django.shortcuts import render

from portfolio.models import Competencia, ContribuicaoOpenSource, Formacao, Licenciatura, Projeto, Tecnologia, TFC, UC


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
