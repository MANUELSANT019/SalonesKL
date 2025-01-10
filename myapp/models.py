from django.db import models

# Create your models here.
# para crear clases de tablas SQL

class Project(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #se asocia con la tabla projects y cuando esta se elmina, se elimina en cascada
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title + ' - ' + self.project.name
