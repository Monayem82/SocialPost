from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from . forms import TwieetForm
from . models import TwieetModel


def twieet_list(request):
    twieet=TwieetModel.objects.all().order_by("-created_at")
    return render(request,'twieet_list.html',{"twieets":twieet})


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


def twieet_delete(request,twieet_id):
    twieet=get_object_or_404(TwieetModel,pk=twieet_id,user=request.user)
    if request.method=="POST":
        twieet.delete()
        return redirect('twieet_list')
    
    return render(request,'delete_twieet.html',{"form":twieet})
