from django import forms
from django.forms import ModelForm
from .models import BugReport
from .models import Task


class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['name', 'description', 'status', 'priority']

