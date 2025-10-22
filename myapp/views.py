from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from myapp.models import Contact
from myapp.forms import ContactForm , NewsLetterForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"website/index.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #for adding my own value for name
            contact = form.save(commit=False)
            contact.name = "Unknown"
            contact.save()
            messages.add_message(request,messages.SUCCESS,"Your ticket submited successfully")
        else:
            messages.add_message(request,messages.ERROR,"Your ticket submited unsuccessfully")
    form = ContactForm()
    return render(request,"website/contact.html",{'form':form})

def about(request):
    return render(request,"website/about.html")

def elements(request):
    return render(request,"website/elements.html")

def newsletter_view(request):
    if request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your email submited successfully")
            return HttpResponseRedirect("/")
        else:
            messages.add_message(request,messages.ERROR,"Your email submited unsuccessfully")
            return HttpResponseRedirect("/")
    form = NewsLetterForm()
    return render(request,"base.html",{"form":form})

def test_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            return HttpResponse("Not Valid")

    form = ContactForm()
    return render(request,"test.html",{"form":form})