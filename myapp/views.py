from django.shortcuts import render , HttpResponse
from myapp.models import Contact
from myapp.forms import NameForm
# Create your views here.
def index(request):
    return render(request,"website/index.html")

def contact(request):
    return render(request,"website/contact.html")

def about(request):
    return render(request,"website/about.html")

def elements(request):
    return render(request,"website/elements.html")

def test_view(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            return HttpResponse("OK")
        else:
            return HttpResponse("Not Valid")

    form = NameForm()
    return render(request,"test.html",{"form":form})