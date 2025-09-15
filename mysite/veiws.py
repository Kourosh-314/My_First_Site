from django.http import HttpResponse
def runserver(request):
    return HttpResponse("Hello")