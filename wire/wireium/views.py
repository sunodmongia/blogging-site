from django.shortcuts import render
from .models import post

# from django.http import HttpResponse


def home(request):
    context ={"posting": post.objects.all()}
    return render(request, "wireium/home.html", context)
    # return HttpResponse('<h1> <center>Home</center></h1>')


def about(request):
    return render(request, "wireium/about.html", {"title": "About"})
    # return HttpResponse('<h1> <center>About</center></h1>')
