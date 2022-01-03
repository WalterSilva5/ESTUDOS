from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.

def pessoa_view(request):
    return render(request, 'pessoa.html')