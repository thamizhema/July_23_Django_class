
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name="login"),
    path('work/',views.work,name="work"),
    path('view/user',views.viewUser,name="info"),
    path('delete/user/<str:id>',views.deleteUser,name="deleteuser"),
    path("update/user/<str:id>",views.updateUser,name='update_user'),
    path("logout/",views.logout,name='logout')

]
