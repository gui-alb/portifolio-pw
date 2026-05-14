from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def registo(request):

    form = RegistoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('landing_page')

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
            return redirect('landing_page')
        else:
            return render(request, 'accounts/login.html', {'mensagem': 'Credenciais inválidas'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('landing_page')