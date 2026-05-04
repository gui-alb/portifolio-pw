from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page_view, name='landing_page'),
    path('home/', views.landing_page_view, name='landing_page'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('contribuicoes/', views.contribuicoesOpenSource_view, name='contribuicoes'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('ucs/', views.unidadeCurricular_view, name='ucs'),
    path('projetos/novo', views.novo_projeto_view, name="novo_projeto"),
    path('tecnologias/novo', views.nova_tecnologia_view, name="nova_tecnologia"),
    path('competencias/novo', views.nova_competencia_view, name="nova_competencia"),
    path('formacoes/novo', views.nova_formacao_view, name="nova_formacao"),


]