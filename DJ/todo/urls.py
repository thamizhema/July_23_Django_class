
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('work/',views.work,name="work"),
    path('about/view/<str:uname>',views.viewUser,name="info"),

]
