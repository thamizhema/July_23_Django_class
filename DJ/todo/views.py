from django.shortcuts import render,HttpResponse

# Create your views here.
def home(req):
    return HttpResponse("<h1>Hi Django</h1>")


def about(req):
    return HttpResponse("<h1>TODO About page</h1>")

