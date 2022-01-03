from django.shortcuts import render
from django.http import HttpResponse
from app.forms import LoginForm

def index(request):
   return render(request, "index.html", {"form": LoginForm()})
