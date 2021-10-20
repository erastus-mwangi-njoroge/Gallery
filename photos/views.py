from django.shortcuts import render
from django.http import HttpResponse, HttpRequest,Http404
from .models import Location, Category, Image


def display_image(request):
    imageResults= Image.objects.all()
    return render(request,"photoviewer/index.html",{'imageResults':imageResults})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photoviewer/search.html',{"message":message,"search_term": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photoviewer/search.html',{"message":message})


def search_category(request):
    location=Location.get_locations()
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        search = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'all-gallery/search-results.html',{"message":message,"category": search,"location":location})
    else:
        return render(request, 'all-gallery/search-results.html')


