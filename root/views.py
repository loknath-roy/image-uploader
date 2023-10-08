
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from.forms import ImageForm
from .models import Image
 


# Create your views here.
def Signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return redirect('signup')
        
        elif username=='' or email=='' or pass1=='' or pass2=='':
            return redirect('signup')

        else:
            user = User.objects.create_user(username,email,pass1)
            user.save()
        
        return redirect('login')

    return render(request,'signup.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
            
    return render(request,'login.html')



def Home(request):
    if request.method=='POST':
        form= ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'home.html',{'form': form,'img':img})

def Logout(request):
    logout(request)
    return redirect('login')









