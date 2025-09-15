from django.urls import path 
from myapp.views import runserver
urlpatterns = [
    path("home/",runserver)
]
