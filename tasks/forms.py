from django import forms
from django.forms import ModelForm
from .models import Project
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assignee']


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')

