from django.urls import path
from . import views

urlpatterns = [
    path('competencias/', views.competencias_view, name='competencias'),
    path('contribuicoes/', views.contribuicoesOpenSource_view, name='contribuicoes'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('ucs/', views.unidadeCurricular_view, name='ucs'),

]