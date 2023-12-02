from django.shortcuts import render, redirect
from .models import ToDo
from django.contrib import messages
from .forms import ToDoCreate, ToDoUpdate


def home(request):
    all = ToDo.objects.all()
    return render(request, 'home.html', {'todos': all})

def details(request,todo_id):
    todo = ToDo.objects.get(id=todo_id)
    return render(request, 'details.html', {'todo': todo})

def delete(request,todo_id):
    ToDo.objects.get(id = todo_id).delete()
    messages.success(request, 'your todo was deleted successfully', 'success')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        form = ToDoCreate(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ToDo.objects.create(title=cd['title'],body=cd['body'],date=cd['date'])
            messages.success(request,'created sucessfully','success')
            return redirect('home')
    form = ToDoCreate()
    return render(request,'create.html',{'form':form})

def update(request,todo_id):
    todo = ToDo.objects.get(id = todo_id)
    if request.method == 'POST':
        form=ToDoUpdate(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'saved','success')
            return redirect('details',todo_id)
    else:
         form = ToDoUpdate(instance=todo)
         return render(request,'update.html',{'form':form})
