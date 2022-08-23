from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from lista.models import ToDo
from lista.forms import ToDoForm

def index(request):
    listas = ToDo.objects.all()
    return render(request, 'index.html', {'listas' : listas} )
    
def indexdetails(request, id):
    lista = get_object_or_404(ToDo, id=id)
    return render(request, 'detail.html', {'lista': lista })

def add(request):
    form = ToDoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'add.html', {'form': form})

def update(request, id):
    lista = ToDo.objects.get(pk=id)
    form = ToDoForm(request.POST or None, instance=lista)
    if form.is_valid():
        form.save()
        return redirect ('index')
    return render(request, 'add.html', {'lista': lista, 'form': form})

def delete(request, id):
    lista = ToDo.objects.get(pk = id)
    lista.delete()
    return redirect('index')