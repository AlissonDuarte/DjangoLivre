from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto

def index(request):

    context = {
        "produtos":Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            messages.success(request, f'Olá {nome},sua mensagem enviada com sucesso. Obrigado pela resposta!')
            form = ContatoForm()
        else:
            messages.error(request, 'Mensagem não enviada, cheque os campos por favor')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Requisição feita com sucesso!")
            form = ProdutoModelForm()
        else:
            messages.error(request, "Erro na requisição")
    else:
        form = ProdutoModelForm()
    context= {
            "form":form
        }
    return render(request, 'produto.html',context)
