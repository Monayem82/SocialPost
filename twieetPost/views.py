from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from . forms import TwieetForm,RegisterUser,loginUserForm
from . models import TwieetModel


def twieet_list(request):
    twieet=TwieetModel.objects.all().order_by("-created_at")
    return render(request,'twieet_list.html',{"twieets":twieet})

@login_required
def create_twieet(request):
    if request.method=="POST":
        form=TwieetForm(request.POST,request.FILES)
        if form.is_valid():
            twieet=form.save(commit=False)
            twieet.user=request.user
            twieet.save()
            return redirect("twieet_list")

    else:
        form=TwieetForm()
    dis={
        "form":form
    }
    return render(request,'create_twieet.html',context=dis)

@login_required
def twieet_edit(request,twieet_id):
    twieet=get_object_or_404(TwieetModel,pk=twieet_id,user=request.user)
    #twieet=TwieetModel.objects.get(id=twieet_id,user=request.user)
    if request.method=="POST":
        form=TwieetForm(request.POST,request.FILES,instance=twieet)
        if form.is_valid():
            twieet=form.save(commit=False)
            twieet.user=request.user
            twieet.save()
            return redirect("twieet_list")

    else:
        form=TwieetForm(instance=twieet)

    dis={
        "form":form
    }
    return render(request,'create_twieet.html',context=dis)

@login_required
def twieet_delete(request,twieet_id):
    twieet=get_object_or_404(TwieetModel,pk=twieet_id,user=request.user)
    if request.method=="POST":
        twieet.delete()
        return redirect('twieet_list') # redirect use class name as the performing class
    
    return render(request,'delete_twieet.html',{"twieet":twieet})


def registerViews(request):
    if request.method=="POST":
        form=RegisterUser(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('twieet_list')
    else:
        form=RegisterUser()
         
    return render(request,'registrations/register.html',{"form":form})


def loginUserViews(request):
    if request.method=="POST":
        form=loginUserForm(request=request,data=request.POST)
        if form.is_valid():
            usern=form.cleaned_data['username']
            passd=form.cleaned_data['password']
            user=authenticate(username=usern,password=passd)
            if user is not None:
                login(request,user)
                return redirect('twieet_list')
    else:
        form=loginUserForm()
    return render(request,'registrations/login.html',{"form":form})


def logoutUserView(request):
    if request.method=='POST':
        logout(request)
        return redirect('twieet_list')
    return redirect('twieet_list')

