from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'XYZ',
        'title':'Blog Post 1',
        'content':'First Post Content ',
        'date_posted':'28 August 2024'
    },
    {
        'author':'ABC',
        'title':'Blog Post 2',
        'content':'Second Post Content ',
        'date_posted':'28 August 2024'
    }
]
# Create your views here.
def home(request):
    context ={
        'posts':posts
    }
    return render(request ,'home.html',context)

def about(request):
    return render(request,'about.html',{'title':'Django About'})
