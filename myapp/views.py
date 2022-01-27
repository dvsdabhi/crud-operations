import imp
from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        User.objects.create(
            name = request.POST['name'],
            email=request.POST['email'],
            mobile = request.POST['mobile'],
            password = request.POST['password'],
        )
        msg = 'User Created'
        many=User.objects.all()
        return render(request,'index.html',{'msg':msg,'many':many})
    many=User.objects.all()
    return render(request,'index.html',{'many':many})

def delete(request,pk):
    uid = User.objects.get(id=pk)
    uid.delete()
    return redirect('index')

def edit(request,pk):
    uid=User.objects.get(id=pk)
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.email =request.POST['email']
        uid.mobile=request.POST['mobile']
        uid.password=request.POST['password']
        uid.save()
        return redirect('index')
    return render(request,'edit.html',{'uid':uid})

    