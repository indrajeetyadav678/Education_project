from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
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
    # print(request.method)
    name= request.POST.get('name')
    email= request.POST.get('email')
    password= request.POST.get('password')
    con_Password= request.POST.get('con_password')
    # print(con_Password)
    # ------------------------------------------
    # tst_Password= request.POST['name']
    # py_data={Name=Name,}
    Registration.objects.create(Name=name,Email=email,Password=password,Con_password=con_Password)
    # msg=("registration successfully done")
    messages.success(request, 'your data successfully register')
    return render(request, 'login.html')

def loginform(request):
    print(request.method)
    username = request.POST.get('username')
    password= request.POST.get('password')
    data1= bool(Registration.objects.filter(Email = username))
    data2=bool(Registration.objects.filter(Password = password))
    if data1 and data2:
        return render(request, 'home.html', {'key':username})
    else:
        return HttpResponse("your Username and password does not exist") 