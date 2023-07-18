from django.shortcuts import render,HttpResponse,redirect
from bson.objectid import ObjectId
import datetime
from .models import uc



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

    if(req.method == "POST"):
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        x = datetime.datetime.now()
       
        data = {"username":username,"email":email,"password":password,"date":x.strftime("%d-%B-%y %X")}
        print(data)
        uc.insert_one(data)
        print("------------------")
        return redirect("work")

    return render(req,'work.html')


def viewUser(req):
    dbData = list(uc.find())
    datas = []
    for i in dbData:
        docId = str(i["_id"])
        i['docId'] = docId
        datas.append(i)
    
    return render(req,'info.html',{"datas":datas})



def deleteUser(req,id):
    print(id,"docId for delete operation")
    uc.delete_one({"_id":ObjectId(id)})
    return redirect("info")
