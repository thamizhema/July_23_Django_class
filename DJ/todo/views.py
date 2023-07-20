from django.shortcuts import render,HttpResponse,redirect
from bson.objectid import ObjectId
import datetime
from .models import uc



# Create your views here.
def home(req):
    print(dict(req.session))
    if( not dict(req.session)):
        return redirect('login')


    return render(req,'home.html',{"name":"python"})

users = [
        {"name":"python","age":20,"email":"py20@gmail.com"},
        {"name":"java","age":20,"email":"java@gmail.com"},
        {"name":"C++","age":20,"email":"CPP@gmail.com"},
        {"name":"dart","age":20,"email":"dart@gmail.com"},
        {"name":"flutter","age":20,"email":"flutter@gmail.com"},
        ]
def about(req):
    if( not dict(req.session)):
        return redirect('login')
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
    if( not dict(req.session)):
        return redirect('login')
    dbData = list(uc.find())
    datas = []
    for i in dbData:
        docId = str(i["_id"])
        i['docId'] = docId
        datas.append(i)
    
    return render(req,'info.html',{"datas":datas})



def deleteUser(req,id):
    if( not dict(req.session)):
        return redirect('login')
    print(id,"docId for delete operation")
    uc.delete_one({"_id":ObjectId(id)})
    return redirect("info")


def updateUser(req,id):
    if( not dict(req.session)):
        return redirect('login')
    userData = uc.find_one({"_id":ObjectId(id)})
    if(req.method == 'POST'):
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        x = datetime.datetime.now()
       
        data = {"username":username,"email":email,"password":password,"updated_time":x.strftime("%d-%B-%y %X")}
        print(data)
        fltr = {"_id":ObjectId(id)}
        uc.update_one(fltr,{"$set":data})
        return redirect('info')
    return render(req,'work.html',{"user":userData})


def login(req):
    if(req.method == "POST"):
        email = req.POST['email']
        user = uc.find_one({"email":email})
        print(user,'===========))))))))))')
        if(user):
            req.session['docId'] = str(user['_id'])
            return redirect('home')
        else:
            return redirect('work')
    return render(req,'login.html')



def logout(req):
    req.session.clear()
    return redirect('home')