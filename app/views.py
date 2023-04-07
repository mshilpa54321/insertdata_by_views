from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserted successfully')

def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    url=input('enter url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('Webpage data is inserted')
    

def insert_AccessRecord(request):
    tn=input('enter tn')
    n=input('enter name')
    url=input('enter url')
    a=input('enter a')
    date=input('enter date')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    ARO=AccessRecord.objects.get_or_create(name=WO,author=a,date=date)[0]
    ARO.save()
    return HttpResponse('AccessRecord data is inserted')

