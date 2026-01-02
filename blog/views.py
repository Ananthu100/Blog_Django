from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#Dummy data
data = [
    {
        'title' : "FIRST BLOG",
        'author' : "Ananthu",
        'content' : "This is my first blog content",
        'date_posted' : "17-12-2025"
    },
    {
        'title' : "SECOND BLOG",
        'author' : "Jacky",
        'content' : "This is my Second blog content",
        'date_posted' : "18-12-2025"
    }
]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})