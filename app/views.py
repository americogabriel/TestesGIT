from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UsuarioForm, Loginform , Cadastroform
from .models import Usuarios
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



def loginpagina(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        encontrado = authenticate(username = nome, password = senha)
        if encontrado:
            try:
                login(request,encontrado)
                return redirect('url_home')
            except Exception as erro:
                return HttpResponse(f"<h1> Não foi possível logar o usuário {erro}")
        else:
            return HttpResponse("<h1> Login não Encontrado")
    data = {}
    data['form'] =  Loginform
    return render(request,'app/login.html',data)

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        primeiro_nome = request.POST.get('primeiro_nome')
        segundo_nome = request.POST.get('segundo_nome')

        verify = authenticate(username = nome, password = senha)

        if verify:
            return HttpResponse("<h1>Credenciais já existentes")
        else:
            try:
                criacao = User.objects.create_user(username = nome, password= senha) # Cria um usuário com o nome e senha passadas
                criacao.first_name = primeiro_nome # Entra no atributo first_name do objeto criado e define como a variável: 'primeiro_nome' 
                criacao.last_name = segundo_nome # Entra no atributo last_name do objeto criado e define com a variável 'segundo_nome'
                criacao.save()
                return redirect('url_login')
            except Exception as erro:
                return HttpResponse(f"<h1> Não foi possível cadastrar o novo usuário. ERROR: {erro}")
    data = {}
    data['form'] = Cadastroform      
    return render(request,'app/cadastrar.html', data)

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nome = request.POST.get('nome')
            idade = request.POST.get('idade')

            Usuarios.objects.create(nome = nome, idade = idade)

            return redirect('url_users')
        
        pessoa_logada = request.user
        data = {}
        data['form'] = UsuarioForm
        data['usuario_nome'] = pessoa_logada.username

        return render(request,'app/home.html',data)
    else:
        return HttpResponse("<h1> É necessário estar logado para acessar essa página")
def listarusers(request):
    
    data = {}
    data['todos_usuarios'] = Usuarios.objects.all()
    return render(request,'app/listar.html',data)
    


