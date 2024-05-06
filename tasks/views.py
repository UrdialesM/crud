from django.shortcuts import render, redirect

from tasks.models import Task
# Create your views here.

def task_list(request):
    tasks = Task.object.all()
    return render(request, tasks/lista-tareas.html, {tasks: tasks})


def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'form-tareas.html')
