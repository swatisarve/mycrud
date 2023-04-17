from django.shortcuts import render, HttpResponse
from mylife.models import Mylife
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Myform

# Create your views here.
def index(request):
    if request.method=='POST':
        age=request.POST.get('age')
        topic=request.POST.get('topic')
        college=request.POST.get('college')
        school=request.POST.get('school')
        rollno=request.POST.get('rollno')
        x=Mylife(age=age, topic=topic, college=college, school=school, rollno=rollno)
        x.save()
    return render(request,'index.html')

def show(request):
    mylife=Mylife.objects.all().values()
    template=loader.get_template('show.html')
    content={
        'mylife':mylife
    }
    return HttpResponse(template.render(content,request))

def update(request,rollno):
    mylife=Mylife.objects.get(rollno=rollno)
    template=loader.get_template('update.html')
    content={
        'mylife':mylife
    }
    return HttpResponse(template.render(content,request))

def updaterecord(request,rollno):
    age=request.POST['age']
    topic=request.POST['topic']
    college=request.POST['college']
    school=request.POST['school']
    rollno=request.POST['rollno']
    mylife=Mylife.objects.get(rollno=rollno)
    mylife.age=age
    mylife.topic=topic
    mylife.college=college
    mylife.school=school
    mylife.rollno=rollno
    mylife.save()
    return HttpResponseRedirect(reverse('show'))

def delete(request,rollno):
    mylife=Mylife.objects.get(rollno=rollno)
    mylife.delete()
    return HttpResponseRedirect(reverse('show'))

def register(request):
    if request.method=='POST':
        form=Myform(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('show'))
        else:
            return render(request,'index.html')
    else:
        form=Myform()
        return render(request,'login.html',{'form':form})    





