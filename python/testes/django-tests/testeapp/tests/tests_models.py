from django.test import TestCase
from testeapp.models import Pessoa

# Create your tests here.
class PessoaTestCase(TestCase):
    #testa a criação de uma pessoa
    def setUp(self):
        Pessoa.objects.create(nome='Joao', idade=20)
    
    
    #testa retorno de nome
    def test_retorno_str(self):
        joao = Pessoa.objects.get(nome='Joao')
        self.assertEqual(joao.nome, 'Joao')