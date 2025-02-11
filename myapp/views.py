from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = 'Bienvenido al sitio de gestión de salas!!'
    return render(request, 'index.html', {'title': title})


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)


def about(request):
    context = {
        "name": "Puestos" 
    }
    return render(request, ('about.html'))


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
   # task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):

    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        print(request.POST)
        project = Project.objects.create(name=request.POST["name"])
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    Project.objects.get(id=id)
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks
        
    })

