from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/create_task.html')


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_complete = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()  # Delete the task from the database
        return redirect('task_list')  # Redirect to the task list page
    return render(request, 'tasks/delete_task.html', {'task': task})
