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

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    return render(request, 'agenda.html', {'eventos': eventos})

@login_required(login_url='/login/')
def evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        usuario = request.user
        try:
            Evento.objects.create(titulo=titulo,
                                descricao=descricao,
                                data_evento=data_evento,
                                usuario=usuario)
            return redirect('/')
        
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar o Evento, erro: {e}')
            return render(request, 'evento.html')
        
    else:
        return render(request, 'evento.html')