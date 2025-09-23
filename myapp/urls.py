from django.urls import path 
from myapp.views import *
urlpatterns = [
    path("",index),
    path("contact/",contact),
    path("about/",about),
    path("elements/",elements)
]
