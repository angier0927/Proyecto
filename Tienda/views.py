from django.shortcuts import render, redirect
from .models import Articulo
from .forms import ArticuloForm

def articulo(request):
    articulos = Articulo.objects.all(),
    ctx = {
        'articulos': articulos,

    }
    return render(request, 'articulos.html', ctx)

def createArticulo(request):
    if request.method == 'GET':
        form = ArticuloForm()
        ctx = {
            'form': form
        }
    else:
        form = ArticuloForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('articulos')


    return render(request, 'manage_articulos.html', ctx)

def editArticulo (request, id):
    articulo = Articulo.objects.get (id = id)
    if request.method == 'GET':
        form = ArticuloForm(instance= articulo)
        ctx = {
            'form' : form
        }
    else:
        form = ArticuloForm(request.POST, instance= articulo)
        ctx = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('articulos')

    return  render(request, 'manage_articulos.html', ctx)

def deleteArticulo(request, id):
    articulo = Articulo.objects.get(id = id)
    articulo.delete()
    return redirect('articulos.html')

