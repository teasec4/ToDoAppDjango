from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


def work_space(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            todos = Todo.objects.filter(user=request.user)
            messages.success(request, ('Task has been added!'))
            return render(request, 'todolist/index.html', {'todos': todos})
    else:
        todos = Todo.objects.filter(user=request.user)
        return render(request, 'todolist/index.html', {'todos': todos})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, ('Task has been Deleted!'))
    return redirect('work_space')


def mark_complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('work_space')


def mark_incomplete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('work_space')


def edit(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        form = TodoForm(request.POST or None, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task has been edited!'))
            return redirect('work_space')
    else:
        todo = Todo.objects.get(id=todo_id)
        return render(request, 'todolist/edit.html', {'todo': todo})


