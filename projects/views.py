from email import message
from importlib.util import resolve_name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ModelForm, ProjectForm
from projects.models import Project
from django.contrib.auth.decorators import login_required
# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html',{'project':projectObj})

@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request,'projects/delete-template.html',context)
    