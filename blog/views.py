from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Dummy data
data = [
    {
        'Title' : "FIRST BLOG",
        'Author' : "Ananthu",
        'Content' : "This is my first blog content",
        'DatePosted' : "17-12-2025"
    },
    {
        'Title' : "SECOND BLOG",
        'Author' : "Jacky",
        'Content' : "This is my Second blog content",
        'DatePosted' : "18-12-2025"
    }
]

def home(request):
    context = {
        'posts' : data
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})