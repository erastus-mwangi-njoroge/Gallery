from django.shortcuts import render
from django.http import HttpResponse, HttpRequest,Http404
from .models import Image,Location,Category

def display_image(request):
    imageResults= Image.objects.all()
    return render(request,"photoviewer/index.html",{'Image':imageResults})