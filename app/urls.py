from django.urls import path
from .views import home,listarusers


urlpatterns = [
    path('',home, name='url_home'),
    path('usuarios/',listarusers, name='url_users'),
]