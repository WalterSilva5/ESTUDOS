from testeapp.models import Pessoa
from django import forms

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'