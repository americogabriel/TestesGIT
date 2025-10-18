from django import forms
from .models import Usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome','idade']

class Loginform(forms.Form):
    nome = forms.CharField(max_length= 100)
    senha = forms.CharField(max_length= 100)

class Cadastroform(forms.Form):
    nome = forms.CharField(max_length= 100)
    senha = forms.CharField(max_length= 100)
    primeiro_nome = forms.CharField(max_length= 100)
    segundo_nome = forms.CharField(max_length= 100)