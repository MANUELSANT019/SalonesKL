from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), #dirección de inicio
    path('about/', views.about, name='about'), #direccion hacia about
    path('hello/<str:username>', views.hello, name='hello'), #direccion hacia hello
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"), #direccion hacia projects
    path('tasks/', views.tasks, name="tasks"), #direccion hacia tasks
    path('create_task/', views.create_task, name="create_task"), #direccion hacia create_task
    path('create_project/', views.create_project, name="create_project"), #direccion hacia create_project
]

#ahora para entrar a las rutas no es necesaria la url completa, solo se necesita el nombre añadido