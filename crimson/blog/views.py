from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
socials = [
    {
        "instagram" : "https://instagram.com/nibble_nb",
        "facebook" : "https://nibble-nb.business.site/",
        "twitter" : "https://twitter.com/nibble_nb",
        "linkedin" : "https://linkedin.com/nibble_nb",
        "github" : "https://github.com/nibble_nb",
    },
    {
        "instagram" : "https://instagram.com/nibble_nb",
        "facebook" : "https://nibble-nb.business.site/",
        "twitter" : "https://twitter.com/nibble_nb",
        "linkedin" : "https://linkedin.com/nibble_nb",
        "github" : "https://github.com/nibble_nb",
    },

]

def home(request):
    return render(request,"blog/index.html")

def about(request):
    #return HttpResponse("<H1>Crimson Blog About</H1>")
    context = {
        'socials':socials,
    }
    return render(request,"blog/about.html",context)