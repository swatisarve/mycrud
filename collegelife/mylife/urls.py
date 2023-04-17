from django.contrib import admin
from django.urls import path
from mylife import views

urlpatterns = [
    # path('index',views.index,name='index'),
    path('',views.show,name='show'),
    path('index',views.index,name='index'),
    path('update/<int:rollno>',views.update,name='update'),
    path('update/updaterecord//<int:rollno>',views.updaterecord,name='updaterecord'),
    path('delete/<int:rollno>',views.delete,name='delete'),
    path('register',views.register,name='register'),
]
