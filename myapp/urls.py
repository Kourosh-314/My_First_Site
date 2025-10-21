from django.urls import path 
from myapp.views import *

app_name = "myapp"

urlpatterns = [
    path("",index,name="index"),
    path("contact/",contact,name="cantact"),
    path("about/",about,name="about"),
    path("elements/",elements,name="elements"),
    path("test/",test_view,name="test")
]
