from django.contrib import admin
from .models import Project, Task
# Register your models here.
#añadir aplicaciones con un panel de administrador como crear datos tec

admin.site.register(Project)
admin.site.register(Task)
