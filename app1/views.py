from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Categoria, Autor, Libro, Prestamo
from .forms import CategoriaForm, AutorForm, LibroForm, PrestamoForm
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def categoria(request, pk=None):
    categorias = Categoria.objects.all()
    if pk:
        delete_url = reverse('categoria-delete', args=[pk])
        edit_url = reverse('categoria-edit', args=[pk])
        instance = get_object_or_404(Categoria, pk=pk)
        if request.path == delete_url:
            instance.delete()
            return redirect('categoria')
        elif request.path == edit_url:
            form = CategoriaForm(request.POST or None, instance=instance)
    else:
        form = CategoriaForm(request.POST or None)
    
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('categoria')
        

    context = {
        'categorias': categorias, 
        'form': form
        }
    return render(request, 'categoria.html', context)



def autor(request, pk=None):
    autores = Autor.objects.all()

    if pk:
        edit_url = reverse('autor-edit', args=[pk])
        delete_url = reverse('autor-delete', args=[pk])

        instance = get_object_or_404(Autor, pk=pk)
        if request.path == edit_url:
            form = AutorForm(request.POST or None, instance=instance)
        elif request.path == delete_url:
            instance.delete()
            return redirect('autor')
    else:
        form = AutorForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')
        
    context = {
        'autores': autores,
        'form': form
    }


    return render(request, 'autor.html', context)



def libro(request, pk=None):
    libros = Libro.objects.all()
    
    if pk:
        edit_url = reverse('libro-edit', args=[pk])
        delete_url = reverse('libro-delete', args=[pk])

        instance = get_object_or_404(Libro, pk=pk)

        if request.path == edit_url:
            form = LibroForm(request.POST or None, instance=instance)
        elif request.path == delete_url:
            instance.delete()
            return redirect('libro')
    else:
        form = LibroForm(request.POST or None)

    
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('libro')
    
    context = {
        'libros': libros,
        'form': form
    }

    return render(request, 'libro.html', context)



def prestamo(request, pk=None):
    prestamos = Prestamo.objects.all()

    if pk: 
        edit_url = reverse('prestamo-edit', args=[pk])
        delete_url = reverse('prestamo-delete', args=[pk])

        instance = get_object_or_404(Prestamo, pk=pk)

        if request.path == edit_url:
            form = PrestamoForm(request.POST or None, instance=instance)
        elif request.path == delete_url:
            instance.delete()
            return redirect('prestamo')
    else:
        form = PrestamoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('prestamo')
    
    context = {
        'form': form,
        'prestamos': prestamos
    }
        

    return render(request, 'prestamo.html', context)