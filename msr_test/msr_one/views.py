from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import *
from .forms import *
# Create your views here.
def projects_details (request, ):
    projects = project_model.objects.all()
    return render(request, "home.html", {"projects": projects})
def project_detail(request, project_id):
    project_det = get_object_or_404(project_model,id=project_id)
    return render(request, "project_detail.html", {"project_det": project_det})
def add_project(request, project_id):
    if request.method == 'POST':
        form = ProjectForm(request.POST, project_id)
        if form.is_valid():
            new_project = form.save()
            return redirect('project_detail', project_id=new_project.id)
    else:
        form = ProjectForm()
    return render(request, "add_project.html", {"form": form})