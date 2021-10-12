from django.shortcuts import render
from django.http import HttpResponse, HttpRequest,Http404
from .models import Location, Category, Image

def display_image(request):
    imageResults= Image.objects.all()
    return render(request,"photoviewer/index.html",{'imageResults':imageResults})