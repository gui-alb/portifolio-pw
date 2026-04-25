from django.shortcuts import render

from portfolio.models import Competencia, ContribuicaoOpenSource, Formacao, Licenciatura, Projeto, Tecnologia, TFC, UC


# Create your views here.
def competencias_view(request):
    competencias = (Competencia.objects
              .select_related()
              .prefetch_related()
              .all())

    return render(request, '', {'competencias': competencias})


def contribuicoesOpenSource_view(request):
    contribuicoes = (ContribuicaoOpenSource.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, '', {'contribuicoes': contribuicoes})


def formacoes_view(request):
    formacoes = (Formacao.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, '', {'formacoes': formacoes})


def licenciaturas_view(request):
    licenciaturas = (Licenciatura.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, '', {'licenciaturas': licenciaturas})


def projetos_view(request):
    projetos = (Projeto.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, '', {'projetos': projetos})


def tecnologias_view(request):
    tecnologias = (Tecnologia.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, '', {'tecnologias': tecnologias})


def tfcs_view(request):
    tfcs = (TFC.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, '', {'tfcs': tfcs})


def unidadeCurricular_view(request):
    ucs = (UC.objects
                    .select_related()
                    .prefetch_related()
                    .all())

    return render(request, '', {'ucs': ucs})
