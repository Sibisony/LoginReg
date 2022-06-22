from contextvars import Context
from django.shortcuts import redirect, render
from accounts.form import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST.get('user')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            return render(request,"login.html",{
                'error_message':'Login Failed Enter Valid username and password',
            })
    return render(request,'login.html')

def register(request):
    form=CreateUserForm()
    Context={'form':form}
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'register.html',Context)

@login_required(login_url='home')    
def profile(request):
    return render(request,'profile.html')  
def logout_page(request):
    logout(request)
    return redirect('home')  

