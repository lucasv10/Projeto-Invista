from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Investimento  # Certifique-se de que a classe é "Investimento" com "I" maiúsculo
from .forms import InvestimentoForm

def pagina_inicial(request):
    return HttpResponse('Pronto para investir')

def contato(request):
    return HttpResponse('para duvidas enviar email para contato@suporte.com')

def minha_historia(request):
    pessoa = {
        'nome': 'jeff',
        'idade': 22,
        'hobby': 'games'
    }
    return render(request, 'investimento/minha_historia.html', pessoa)

def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimento/investimentos.html', dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimento/detalhe.html', dados)

def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_Form = InvestimentoForm()
        formulario = {
            'formulario': investimento_Form
        }
        return render(request, 'investimento/novo_investimento.html', context=formulario)

def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimento/novo_investimento.html', {'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')

def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')  # Corrigido o nome da URL
    return render(request, 'investimento/confirmar_exclusao.html', {'item': investimento})
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Investimento  # Certifique-se de que a classe é "Investimento" com "I" maiúsculo
from .forms import InvestimentoForm

def pagina_inicial(request):
    return HttpResponse('Pronto para investir')

def contato(request):
    return HttpResponse('para duvidas enviar email para contato@suporte.com')

def minha_historia(request):
    pessoa = {
        'nome': 'jeff',
        'idade': 22,
        'hobby': 'games'
    }
    return render(request, 'investimento/minha_historia.html', pessoa)

def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimento/investimentos.html', dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimento/detalhe.html', dados)

def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_Form = InvestimentoForm()
        formulario = {
            'formulario': investimento_Form
        }
        return render(request, 'investimento/novo_investimento.html', context=formulario)

def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimento/novo_investimento.html', {'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')

def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')  # Corrigido o nome da URL
    return render(request, 'investimento/confirmar_exclusao.html', {'item': investimento})
