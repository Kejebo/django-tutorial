from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required

@login_required
def init(request):
    person=Person.objects.all()
    return render(request,"home.html",{'persons':person})

@login_required
def insert(request):
    if(request.method=='GET'):
        contex={
            'form':PersonForm
        }
    else:
        form= PersonForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('app_persons:home')
            
    return render(request,'insert.html',contex)

@login_required
def update(request,id):
    person=Person.objects.get(id=id)
    if request.method=='GET':
        form=PersonForm(instance=person)
        return render(request,'insert.html',{'form':form})
    else:
        form= PersonForm(request.POST,instance=person)   
        if form.is_valid():
            form.save()
            return redirect('app_persons:home')
            
    return render(request,'insert.html',contex)

@login_required
def delete(request,id):
    person=Person.objects.get(id=id)
    person.delete()
    
    return redirect('app_persons:home')