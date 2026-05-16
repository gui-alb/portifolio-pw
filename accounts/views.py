from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import *

def registo(request):
    form = RegistoForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        autores_group, created = Group.objects.get_or_create(name='autores')
        user.groups.add(autores_group)
        login(request, user)
        return redirect('lista_artigos')

    return render(request, 'accounts/registo.html', {'form': form})

def login_view(request):

    if request.POST:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )

        if user:
            login(request, user)
            return redirect('lista_artigos')
        else:
            return render(request, 'accounts/login.html', {'mensagem': 'Credenciais inválidas'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('lista_artigos')