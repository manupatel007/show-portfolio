from django.shortcuts import render
from projects.models import Project
# Create your views here.

def proj_index(request):
    v1 = Project.objects.all()
    context = {
        'projects':v1
    }
    return render(request,'proj_index.html',context)

def proj_detail(request,pk):
    v1 = Project.objects.get(pk=pk)
    context = {
        'projects':v1
    }
    return render(request,'proj_detail.html',context)