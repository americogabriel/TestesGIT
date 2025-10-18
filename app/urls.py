from django.urls import path
from .views import home,listarusers,loginpagina,cadastrar


urlpatterns = [
    path('',loginpagina, name = 'url_login'),
    path('cadastro/',cadastrar, name = 'url_cadastrar'),
    path('home/',home, name='url_home'),
    path('usuarios/',listarusers, name='url_users'),
]