from django.db import models

class Usuarios(models.Model):
    nome = models.TextField(max_length= 50)
    idade = models.IntegerField()
