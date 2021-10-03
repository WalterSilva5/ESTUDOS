from django import forms

class LoginForm(forms.Form):
    nome = forms.CharField(label="Nome")
    senha = forms.CharField(widget=forms.PasswordInput())    