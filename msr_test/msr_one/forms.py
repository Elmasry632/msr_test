from django import forms
from .models import *

class ProjectForm(forms.Form):
    project_name = forms.CharField(max_length=30, label="Project Name")
    description = forms.CharField(widget=forms.Textarea, max_length=150, label="Project Description")
