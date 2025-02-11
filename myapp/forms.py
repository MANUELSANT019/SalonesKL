from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=255, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label='descripción de la tarea', widget=forms.Textarea)


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Name project", max_length=200)