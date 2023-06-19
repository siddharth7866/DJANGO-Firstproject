from django.shortcuts import render
from django.http import HttpResponse
from register.forms import NewUser


# Create your views here.
def index(request):
    return render(request,'index.html')

def user(request):
    form=NewUser()
    if request.method=='POST':
        form=NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("error")
    return render(request,'user.html',{'form':form})
