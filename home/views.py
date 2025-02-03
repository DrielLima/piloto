# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')

def ajuda(request):
    return render(request,'ajuda.html')

def local(request):
    return render(request,'local.html')

def exibiritem(request,id):
    return render(request,'exibiritem.html',{'id':id})

def perfil(request):
    return render(request,'perfil.html')

