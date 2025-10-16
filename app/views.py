from django.shortcuts import render
from django.http import HttpResponse
from .forms import UsuarioForm

def home(request):
    data = {}
    data['form'] = UsuarioForm
    return render(request,'app/home.html',data)



