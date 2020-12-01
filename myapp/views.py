from django.shortcuts import render
from myapp.models import BlogApp

def BlogView(request):

    blog = BlogApp.object.all()
    
    return render(request,'myapp/index.html',{'Nilesh':blog})
