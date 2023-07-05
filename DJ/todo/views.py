from django.shortcuts import render,HttpResponse

# Create your views here.
def home(req):
    return render(req,'home.html',{"name":"python"})


def about(req):
    return render(req,'about.html',{"isDone":'z'})

def work(req):
    return render(req,'work.html')

