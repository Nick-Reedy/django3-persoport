from django.shortcuts import render
from .models import Project
from .models import Archive

def home(request):
    projects = Project.objects.all()
    return render(request, "portfolio\home.html", {"projects":projects})
# Create your views here.
def pros(request):
    projects = Project.objects.all()
    return render(request, "portfolio\pros.html", {"projects":projects})

def library(request):
    archives = Archive.objects.all()
    return render(request, "portfolio\library.html", {"archives":archives})
