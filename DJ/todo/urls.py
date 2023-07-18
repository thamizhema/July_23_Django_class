
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('work/',views.work,name="work"),
    path('view/user',views.viewUser,name="info"),
    path('delete/user/<str:id>',views.deleteUser,name="deleteuser"),

]
