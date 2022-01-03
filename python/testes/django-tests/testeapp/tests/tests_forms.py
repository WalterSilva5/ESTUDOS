from django.test import TestCase
from testeapp.forms import PessoaForm

class PessoaFormtestCase(TestCase):
    def test_pessoa_form_valid(self):
        form = PessoaForm(data = {
            'nome': 'Teste',
            'idade': 15,
        })
        self.assertTrue(form.is_valid())
    
    def test_pessoa_form_invalid(self):
        form = PessoaForm(data = {
        })
        self.assertFalse(form.is_valid())    
    