from django.shortcuts import render
from rest_framework import viewsets
from clientes.models import Cadastro
from clientes.serializers import CadastroSerializer

class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
    
