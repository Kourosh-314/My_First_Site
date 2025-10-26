from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
def login_view(request):
    #Adding a another form of getting user authenticated besides in login html page
    if not request.user.is_authenticated: 
        if request.method =='POST':
            form = AuthenticationForm(request = request,data = request.POST)
            if form.is_valid(): 
                username = form.cleaned_data.get['Username']
                password = form.cleaned_data.get['Password']
                user = authenticate(request, username=username, password=password)
                #Cheking if the user is not in the database
                if user is not None:
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,"You logged in seccessfully")
                    return redirect('/')
        form = AuthenticationForm()
        context = {"form":form}
        return render(request,'accounts/login.html',context)
    else:
        messages.add_message(request,messages.SUCCESS,"You have already logged in successfuly")
        return redirect('/')
    

def logout_view(request):
    return render(request,'accounts/logout.html')
def signup_view(request):
    return render(request,'accounts/signup.html')