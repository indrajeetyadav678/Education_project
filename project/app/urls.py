from django.urls import path
from .views import*

urlpatterns=[
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('course/', course, name='course'),
    path('courses/', courses, name='courses'),
    path('elements/', elements, name='elements'),
    path('blog/', blog, name='blog'),
    path('blog_detail/', blog_detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
]