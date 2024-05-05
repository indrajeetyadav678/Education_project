from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def course(request):
    return render(request, 'Course.html')

def courses(request):
    return render(request, 'courses.html')

def elements(request):
    return render(request, 'Element.html')

def blog(request):
    return render(request, 'blog.html')


def blog_detail(request):
    return render(request, 'blog_detail.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')