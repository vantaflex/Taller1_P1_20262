from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Bienvenido a home</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name':'David Santiago Duarte'})

def about(request):
    return HttpResponse("<h1>Welcome to About Page</h1>")