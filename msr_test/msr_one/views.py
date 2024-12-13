from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import *

# Create your views here.
def projects_details (request, ):
    projects = project_model.objects.all()
    return render(request, "home.html", {"projects": projects})



def project_detail(request, project_id):
    project_det = get_object_or_404(project_model,id=project_id)
    return render(request, "project_detail.html", {"project_det": project_det})