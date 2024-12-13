from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import *

# Create your views here.
def msr_one (request):
    project = get_object_or_404(project_model)
    return render(request, "home.html", {"project": project})