from django.shortcuts import render, redirect
from portfolio.models import Project, NewFields, FollowersField, FollowingField, NotificationsField
from portfolio.forms import AddProject, AddFields
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
#from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def portfolio(request):
    personp = request.user.username
    dbba = Project.objects.filter(person__username__contains=personp)
    info = NewFields.objects.filter(person__username__contains=personp)
    followers = FollowersField.objects.filter(person__username__contains=personp).count()
    following = FollowingField.objects.filter(person__username__contains=personp).count()
    #notifications = NotificationsField.objects.filter(person__username__contains=personp)
    context = {
        'dbba':dbba,
        'info':info,
        'followers':followers,
        'following':following,
        #'notifications':notifications,
    }
    return render(request,'portfolio.html',context)

@login_required
def addproject(request,personp):
    #notifications = NotificationsField.objects.filter(person__username__contains=personp)
    if request.method == 'GET':
        context = {
            'form': AddProject,
            #'notifications': notifications,
        }
        return render(request,'addproject.html', context)
    else:
        form = AddProject(request.POST, request.FILES)
        if form.is_valid():
            sup=Project(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'], 
            technology=form.cleaned_data['technology'],
            person=request.user, 
            main_image=form.cleaned_data['main_image'],
            source_code=form.cleaned_data['source_code'],
            img1 = form.cleaned_data['img1'],
            img2 = form.cleaned_data['img2'],
            img3 = form.cleaned_data['img3'],
            )
        #g1 = Project()
            print(sup)
            sup.save()
            #yha bhari cheez ane wali h(notifications)
            User = get_user_model()
            val = FollowersField.objects.filter(person__username__contains=request.user.username)
            sending_person = NewFields.objects.filter(person__username__contains=request.user.username)[0]
            for v in val:
                user1 = User.objects.filter(username=v.followers)[0]
                #user1 = NewFields.objects.filter(person__username__contains=v.followers)[0]
                shi_dbba = NotificationsField(person=user1, sender=sending_person, Pid=sup.id, notifications=request.user.username+" recently added a project")
                shi_dbba.save()
                print(shi_dbba.notifications)
            dbba = Project.objects.filter(person__username__contains=personp)
            info = NewFields.objects.filter(person__username__contains=personp)
            context = {
                'dbba':dbba,
                'info':info,
            }
            #return render(request,'portfolio.html',context)
            return redirect(reverse('portfolio'))
@login_required
def completeprofile(request, personp):
    if request.method == 'GET':
        context = {
            'form': AddFields,
        }
        return render(request,'addfields.html', context)
    elif request.method == 'POST':
        form = AddFields(request.POST, request.FILES)
        if form.is_valid():
            if NewFields.objects.filter(person__username__contains=personp):
                nyi_info = NewFields.objects.get(person__username__contains=personp)
                nyi_info.skills=form.cleaned_data['skills']
                nyi_info.location=form.cleaned_data['location'] 
                nyi_info.contact=form.cleaned_data['contact']
                #nyi_info.person=request.user,
                nyi_info.bio = form.cleaned_data['bio']
                nyi_info.profile_pic=form.cleaned_data['profile_pic']
                nyi_info.save()
                return redirect(reverse('portfolio'))
            else:
                if form.is_valid():
                    sup=NewFields(
                    skills=form.cleaned_data['skills'],
                    location=form.cleaned_data['location'], 
                    contact=form.cleaned_data['contact'],
                    person=request.user,
                    bio = form.cleaned_data['bio'], 
                    profile_pic=form.cleaned_data['profile_pic'],
                    )
                    print(sup)
                    sup.save()
                    dbba = Project.objects.filter(person__username__contains=personp)
                    info = NewFields.objects.filter(person__username__contains=personp)
                    context = {
                        'dbba':dbba,
                        'info':info,
                    }
                    #return render(request,'portfolio.html',context)
                    return redirect(reverse('portfolio'))
                else:
                    return HttpResponse("Unsuccessfull")

@login_required
def project_detail(request,pk,personp):
    dbba = Project.objects.filter(id=pk)
    info = NewFields.objects.filter(person__username__contains=personp)
    #notifications = NotificationsField.objects.filter(person__username__contains=personp)
    context = {
                'dbba':dbba,
                'info':info,
                #'notifications':notifications,
            }
    return render(request,'project_detail.html',context)

@login_required
def project_home(request):
    dbba = Project.objects.all()
    context = {
        'dbba':dbba,
    }
    return render(request,'project_home.html',context)

@csrf_exempt
def project_describe(request, pk):
    dbba = Project.objects.filter(id=pk)
    personp = dbba[0].person.username
    if(personp==request.user.username):
        info = NewFields.objects.filter(person__username__contains=personp)
        context = {
                    'dbba':dbba,
                    'info':info,
                }     
        return render(request,'project_detail.html',context)
    else:
        if request.method == 'POST':
            val = FollowingField(person=request.user, following=personp)
            val.save()
            User = get_user_model()
            user1 = User.objects.filter(username=personp)[0]
            val = FollowersField(person=user1, followers=request.user.username)
            val.save()
            info = NewFields.objects.filter(person__username__contains=personp)
            context = {
                        'dbba':dbba,
                        'info':info,
                        'bool':True,
                    }
            return render(request,'project_describe.html',context)

        else:
            info = NewFields.objects.filter(person__username__contains=personp)
            val = FollowersField.objects.filter(person__username__contains=personp,followers=request.user.username)
            if val:
                context = {
                            'dbba':dbba,
                            'info':info,
                            'bool':True,
                        }
                return render(request,'project_describe.html',context)
            else:
                context = {
                            'dbba':dbba,
                            'info':info,
                            'bool':False,
                        }
                return render(request,'project_describe.html',context)

def followers(request):
    dbba = FollowersField.objects.filter(person__username__contains=request.user.username)
    context = {
        'dbba':dbba,
    }
    return render(request,'followers.html', context)

def following(request):
    dbba = FollowingField.objects.filter(person__username__contains=request.user.username)
    context = {
        'dbba':dbba,
    }
    return render(request,'following.html', context)


def other_followers(request,personp):
    dbba = FollowersField.objects.filter(person__username__contains=personp)
    context = {
        'dbba':dbba,
    }
    return render(request,'followers.html', context)

def other_following(request,personp):
    dbba = FollowingField.objects.filter(person__username__contains=personp)
    context = {
        'dbba':dbba,
    }
    return render(request,'following.html', context)


def notifications(request):
    dbba = NotificationsField.objects.filter(person__username__contains=request.user.username)
    context = {
        'dbba':dbba,
    }
    return render(request,'notifications.html', context)

class NotificationCheck(View):
    def get(self, request):
        return HttpResponse(NotificationsField.objects.all().count())

def view_portfolio(request, personp):
    #personp = request.user.username
    if(personp==request.user.username):
        personp = request.user.username
        dbba = Project.objects.filter(person__username__contains=personp)
        info = NewFields.objects.filter(person__username__contains=personp)
        followers = FollowersField.objects.filter(person__username__contains=personp).count()
        following = FollowingField.objects.filter(person__username__contains=personp).count()
        #notifications = NotificationsField.objects.filter(person__username__contains=personp)
        context = {
            'dbba':dbba,
            'info':info,
            'followers':followers,
            'following':following,
            #'notifications':notifications,
        }
        return render(request,'portfolio.html',context)
    else:
        if request.method == 'POST':
            val = FollowingField(person=request.user, following=personp)
            val.save()
            User = get_user_model()
            user1 = User.objects.filter(username=personp)[0]
            val = FollowersField(person=user1, followers=request.user.username)
            val.save()
            #info = NewFields.objects.filter(person__username__contains=personp)
            dbba = Project.objects.filter(person__username__contains=personp)
            dbbu = dbba[0]
            info = NewFields.objects.filter(person__username__contains=personp)
            followers = FollowersField.objects.filter(person__username__contains=personp).count()
            following = FollowingField.objects.filter(person__username__contains=personp).count()
            context = {
                'dbba':dbba,
                'info':info,
                'followers':followers,
                'following':following,
                'dbbu':dbbu,
                'bool':True,
                #'notifications':notifications,
            }
            return render(request,'view_portfolio.html',context)
        else:
            val = FollowersField.objects.filter(person__username__contains=personp,followers=request.user.username)
            dbba = Project.objects.filter(person__username__contains=personp)
            dbbu = dbba[0]
            info = NewFields.objects.filter(person__username__contains=personp)
            followers = FollowersField.objects.filter(person__username__contains=personp).count()
            following = FollowingField.objects.filter(person__username__contains=personp).count()
            #notifications = NotificationsField.objects.filter(person__username__contains=personp)
            if val:
                context = {
                    'dbba':dbba,
                    'info':info,
                    'followers':followers,
                    'following':following,
                    'dbbu':dbbu,
                    'bool':True,
                    #'notifications':notifications,
                }
                return render(request,'view_portfolio.html',context)
            else:
                context = {
                    'dbba':dbba,
                    'info':info,
                    'followers':followers,
                    'following':following,
                    'dbbu':dbbu,
                    'bool':False,
                    #'notifications':notifications,
                }
                return render(request,'view_portfolio.html',context)