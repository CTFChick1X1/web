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
    return render(request, 'portfolio.html')


def blogpost(request):
    return render(request, 'blogpost.html')