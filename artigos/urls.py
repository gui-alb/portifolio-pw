from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artigos, name='lista_artigos'),
    path('artigo/<int:artigo_id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('novo/', views.novo_artigo, name='novo_artigo'),
    path('editar/<int:artigo_id>/', views.edita_artigo, name='edita_artigo'),
    path('like/<int:artigo_id>/', views.like_artigo, name='like_artigo'),
]
