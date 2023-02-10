from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


#outra forma de direcionar a url direto para a pagina agenda
#def index(request):
#    return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)          #já existe uma função no django de logout
    return redirect('/')     #vai direcionar para o indice
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')    #paramentro que quer recuperar do login
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')     #vai direcionar para o indice
        else:
            messages.error(request, "Usuario ou senha inválido")
    return redirect('/')

@login_required(login_url='/login/')   #quando nao estiver autenticado vai levar para esse endereço
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) # define filtro para o usuario logado
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')   #solicitar o login para criar novo evento
def evento(request):
    return render(request, 'evento.html')      #encaminha para pagina de novo evento

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')     #usando o mesmo nome do html
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,              #ver models / esta criando novo evento
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')