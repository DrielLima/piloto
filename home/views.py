# Create your views here.
from django.shortcuts import render, HttpResponse

LISTA_ALUNOS = [
    {"nome": "João Silva", "matricula": "202301","data": "03/10/2009","curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Maria Oliveira", "matricula": "202302","data": "05/02/2008", "curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Carlos Souza", "matricula": "202303","data": "20/12/2009", "curso": "Técnico em Informática", "turma": "208"},
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

from django.shortcuts import redirect

def editar_aluno(request, indice):
    aluno = LISTA_ALUNOS[indice]  # Obtém a referência do aluno na lista


    if request.method == "POST":
        # Atualiza diretamente os valores do dicionário aluno
        aluno['nome'] = request.POST.get("nome")
        aluno['matricula'] = request.POST.get("matricula")
        aluno['curso'] = request.POST.get("curso")
        aluno['turma'] = request.POST.get("turma")


        return redirect('listar_alunos')  # Redireciona para a lista de alunos


    context = {
        'aluno': aluno,
        'indice': indice
    }
    return render(request, 'from_aluno.html', context)

def cadastrar_aluno(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        matricula = request.POST.get("matricula")
        curso = request.POST.get("curso")
        turma = request.POST.get("turma")


        novo_aluno = {
            "nome": nome,
            "matricula": matricula,
            "curso": curso,
            "turma": turma
        }
        LISTA_ALUNOS.append(novo_aluno)  # Adiciona o novo aluno à lista


        return redirect('listar_alunos.html')  # Redireciona para a lista de alunos


    return render(request, 'from_aluno.html')  # Exibe o formulário vazio







