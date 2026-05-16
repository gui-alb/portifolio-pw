from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm

def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/lista_artigos.html', {'artigos': artigos})

def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.all().order_by('-data_criacao')
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            return redirect('detalhe_artigo', artigo_id=artigo.id)
    else:
        form = ComentarioForm()

    return render(request, 'artigos/detalhe_artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form
    })

def e_autor(user):
    return user.groups.filter(name='autores').exists()

@login_required
@user_passes_test(e_autor)
def novo_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('lista_artigos')
    else:
        form = ArtigoForm()
    return render(request, 'artigos/form_artigo.html', {'form': form, 'titulo': 'Novo Artigo'})

@login_required
@user_passes_test(e_autor)
def edita_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    
    if artigo.autor != request.user:
        return redirect('lista_artigos')

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('lista_artigos')
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/form_artigo.html', {'form': form, 'titulo': 'Editar Artigo'})

def like_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.user.is_authenticated:
        if request.user in artigo.likes.all():
            artigo.likes.remove(request.user)
        else:
            artigo.likes.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', 'lista_artigos'))
