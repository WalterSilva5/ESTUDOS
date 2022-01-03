from rest_framework import serializers
from app.models import Pessoa

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['nome', 'altura']
        
    