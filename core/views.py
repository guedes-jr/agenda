from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.POST:
        usuario = request.POST.get('usuario')    
        senha = request.POST.get('senha')    
        usuario = authenticate(username=usuario, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e/ou senha inválidos!')
            
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(ususario=usuario)
    return render(request, 'agenda.html', {'eventos': eventos})