from django.shortcuts import render
from .models import*
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

def signup(request):
    return render(request, 'registration.html')

def regist(request):
    print(request.method)
    name= request.POST.get('name')
    email= request.POST.get('name')
    password= request.POST.get('name')
    con_Password= request.POST.get('name')
    # ------------------------------------------
    # tst_Password= request.POST['name']
    # py_data={Name=Name,}
    Registration.create(
        {
        'Name':'name',
        'Email':'email',
        'Password':'password',
        'Con_password':'con_Password'
        }
    )
    return render(request, 'login.html')