from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Bishwash',
        'title': 'Blog Post 1',
        'content': 'first post',
        'date_posted': 'september 2020'
    },
    {
        'author': 'Bish',
        'title': 'Blog Post 2',
        'content': 'second post',
        'date_posted': 'september 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

