from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from Todo.models import *


def index(request):
    tasks = Task.objects.all().order_by('end_date')
    categories = Category.objects.all()
    contex = {
        'tasks': tasks,
        'categories': categories
    }
    return render(request, 'Todo/index.html', contex)


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    categories = Category.objects.all()

    if request.method == "POST":
        task.title = request.POST.get('name')
        task.description = request.POST.get('description')
        task.end_date = request.POST.get('end_date')
        task.category_id = request.POST.get('category')
        task.save()
        return redirect('index')

    context = {
        'task': task,
        'categories': categories
    }
    return render(request, 'Todo/update_task.html', context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('index')  # Redirect back to the task list view
    return render(request, 'Todo/delete_task.html', {'task': task})
