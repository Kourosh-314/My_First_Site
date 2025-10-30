from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from accounts.forms import *
# Create your views here.

def login_view(request):
    #Adding a another form of getting user authenticated besides in login html page
    if not request.user.is_authenticated: 
        if request.method =='POST':
            form = EmailOrUsernameAuthForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                #Cheking if the user is not in the database
                if user is not None:
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,"You logged in successfully")
                    return redirect('/')
            else:
                messages.add_message(request,messages.ERROR ,"Invalid email/username or password")
        else:
            form = EmailOrUsernameAuthForm()

        context = {"form":form}
        return render(request,'accounts/login.html',context)
    else:
        messages.add_message(request,messages.SUCCESS,"You have already logged in successfuly")
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,"You logged out successfully")
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,"You signed up successfully")
                return redirect('accounts:login')
            else:
                messages.add_message(request,messages.ERROR ,"Please correct the errors below")
        else:
            form = CustomUserCreationForm()

        context = {"form":form}
        return render(request,'accounts/signup.html',context)
    else:
        messages.add_message(request,messages.SUCCESS,"You have already signed up successfully")
        return redirect('myapp:index')
    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('accounts:password_reset_done')
    
    def form_valid(self, form):
        messages.success(self.request, "Password reset email has been sent.")
        return super().form_valid(form)

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    
    def form_valid(self, form):
        messages.success(self.request, "Your password has been reset successfully.")
        return super().form_valid(form)

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'