from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        msg = 'User is authenticated as {}'.format(request.user.username)
    else:
        msg = 'User is not authenticated'

    return render(request,'accounts/login.html',{'msg':msg})

def logout_view(request):
    return render(request,'accounts/logout.html')
def signup_view(request):
    return render(request,'accounts/signup.html')