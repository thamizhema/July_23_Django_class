from django.shortcuts import render,HttpResponse

# Create your views here.
def home(req):
    return render(req,'home.html',{"name":"python"})

users = [
        {"name":"python","age":20,"email":"py20@gmail.com"},
        {"name":"java","age":20,"email":"java@gmail.com"},
        {"name":"C++","age":20,"email":"CPP@gmail.com"},
        {"name":"dart","age":20,"email":"dart@gmail.com"},
        {"name":"flutter","age":20,"email":"flutter@gmail.com"},
        ]
def about(req):
   
    return render(req,'about.html',{"isDone":'z',"users":users})

def work(req):
    return render(req,'work.html',{"data":["s",1,2,3,4]})


def viewUser(req,uname):
    print(uname)
    ud = {}
    for i in users:
        if(i['name'] == uname):
            ud = i
            break
    return render(req,'info.html',{"info":ud})


