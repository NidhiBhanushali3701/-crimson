from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
    return render(request,"blog/index.html")

def about(request):
    #return HttpResponse("<H1>Crimson Blog About</H1>")
    context = {
        'socials': Post.objects.all(),
    }
    return render(request,"blog/about.html",context)