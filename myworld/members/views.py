from multiprocessing import context
from telnetlib import AUTHENTICATION
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Student
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse 

# Create your views here.
def index(request):
    template = loader.get_template('template.html')
    return HttpResponse(template.render({}))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))
def addrecord(request):
    x = request.POST['BrandName']
    y = request.POST['OriginCountry']
    member = Student(BrandName=x, OriginCountry=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def delete(request):
  id=request.POST['id']
  try:
    mymember = Student.objects.get(id=id)
    mymember.delete()
    return HttpResponseRedirect(reverse('index'))
  except:
    return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def update(request):
  id=request.POST['id']
  try:
    mymember = Student.objects.get(id=id)
  except:
    mymember=0
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,'id':id,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['BrandName']
  last = request.POST['OriginCountry']
  member = Student.objects.get(id=id)
  member.BrandName = first
  member.OriginCountry = last
  member.save()
  return HttpResponseRedirect(reverse('index'))

def searchRecord(request):
    x = request.GET['OriginCountry']
    if x=='all' or x=='All':
      mydata = Student.objects.filter().all()
      print(mydata)
    else:
      mydata = Student.objects.filter(OriginCountry=x)
    template = loader.get_template('search.html')
    context = {
        'mymember': mydata,'xid':x,
        }
    return HttpResponse(template.render(context))


    

