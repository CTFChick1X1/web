from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    portfolio = Project.objects.all()
    blogpost = BlogPost.objects.all().order_by('-created_at')[:3]

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    projects = Project.objects.select_related('category').all()
    return render(request, 'portfolio.html', {'projects': projects})


def blogpost(request):
    blogposts = BlogPost.objects.select_related('author').all()
    return render(request, 'blogpost.html', {'blogposts': blogposts})
