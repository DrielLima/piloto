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

def perfil(request,usuario):
    return render(request,'perfil.html', {'usuario':usuario})

def dados(request):
    context = {
        'nome': 'João',
        'idade': 16,
        'cidade': 'Teresina'
    }
    return render(request,'dados.html',context)


