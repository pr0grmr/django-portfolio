from django.shortcuts import render
from .models import Projects


# Create your views here.
def home(request):
    projects = Projects.objects.all()
    dict = {"projects": projects}
    return render(request, "base/home.html", dict)


def about(request):
    return render(request, "base/about.html")


def projects(request, pk):
    project = Projects.objects.get(id=pk)
    dict = {"project": project}
    return render(request, "base/projects.html", dict)
