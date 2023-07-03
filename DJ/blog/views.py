from django.shortcuts import render,HttpResponse

# Create your views here.

def home(req):
    return HttpResponse("<button>This is Blog app</button>")
