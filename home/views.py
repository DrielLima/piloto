# Create your views here.
from django.shortcuts import render, HttpResponse

LISTA_ALUNOS = [
    {"nome": "João Silva", "matricula": "202301", "curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Maria Oliveira", "matricula": "202302", "curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Carlos Souza", "matricula": "202303", "curso": "Técnico em Informática", "turma": "208"},
]

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
def form(request):
    if request.method == "POST": 
        # captura cada informação digitada no formulário
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        cidade = request.POST.get("cidade")
        # cria um dicionário context com os dados capturados
        context = {
            'nome': nome,
            'idade': idade,
            'cidade': cidade
        }
        # mostra os dados capturados no template dados.html
        return render(request,'dados.html',context)
    else: # method GET, mostra o formulário vazio
        return render(request,'form.html')
def listar_alunos(request):
    context = {
        'lista': LISTA_ALUNOS,
    }
    return render(request, 'listar_alunos.html', context) 



