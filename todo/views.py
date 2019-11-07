from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST

# Create your views here.

def Todo_list(request):
    todo_list=Todo.objects.order_by('id')
    form= TodoForm()
    context={'todo_list':todo_list, 'form':form}
    return render(request,'todo/Todo_list.html', context)
    
# this view only accepts post requests
@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('Todo_list')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('Todo_list')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('Todo_list')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('Todo_list')

# @require_EDIT
# def editTodo(request, pk):
#     todo = Todo.objects.get(pk=todo_id)
#     if request.method == "POST":
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid():
#             todo = form.save()
#             return redirect('Todo_list', pk=todo.pk)
#     else:
#         form = TodoForm(instance=todo)
#     return render(request, 'todo/Todo_list.html', {'form': form})