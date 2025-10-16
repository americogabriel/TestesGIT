from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UsuarioForm
from .models import Usuarios

def home(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        Usuarios.objects.create(nome = nome, idade = idade)
        return redirect('url_users')
    data = {}
    data['form'] = UsuarioForm
    return render(request,'app/home.html',data)

def listarusers(request):
    data = {}
    data['todos_usuarios'] = Usuarios.objects.all()
    return render(request,'app/listar.html',data)


