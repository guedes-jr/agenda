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
    id_evento = request.GET.get('id')
    dados = {}
    
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
        
    if request.POST:
        titulo = request.POST.get('titulo')
        local = request.POST.get('local')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        usuario = request.user
        id_evento = request.POST.get('id_evento') \
                        if request.POST.get('id_evento') \
                            else None
        try:
            if usuario == request.user:
                new_evento = Evento(id=id_evento,
                                    titulo=titulo,
                                    local=local,
                                    descricao=descricao,
                                    data_evento=data_evento,
                                    usuario=usuario)
                new_evento.save()
            else:
                messages.error(request, f'Apenas o jusuário {usuario} pode alterar esse evento!')
            return redirect('/')
        
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar o Evento, erro: {e}')
            return render(request, 'evento.html')
        
    else:
        return render(request, 'evento.html', dados)


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if evento.usuario == usuario:
        evento.delete()
    else:
        messages.error(request, f'Evento não pertence a usuário {usuario}!')
    return redirect('/')