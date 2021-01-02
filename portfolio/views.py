from django.shortcuts import render, redirect
from portfolio.models import Project
from portfolio.forms import AddProject
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def portfolio(request,personp):
    dbba = Project.objects.filter(person=personp)
    context = {
        'dbba':dbba,
    }
    return render(request,'portfolio.html',context)

def addproject(request,personp):
    if request.method == 'GET':
        context = {
            'form': AddProject,
        }
        return render(request,'addproject.html', context)
    else:
        form = AddProject(request.POST, request.FILES)
        if form.is_valid():
            sup=Project(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'], 
            technology=form.cleaned_data['technology'],
            person=personp, 
            image=form.cleaned_data['image'])
        #g1 = Project()
            print(sup)
            sup.save()
            dbba = Project.objects.filter(person=personp)
            context = {
                'dbba':dbba,
            }
            return render(request,'portfolio.html',context)
