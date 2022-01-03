from django.shortcuts import render
from rest_framework import viewsets
from app.models import Pessoa
# Create your views here.
from app.serializers import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    