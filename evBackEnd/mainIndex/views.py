
from random import Random, randint, random
from statistics import mode
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    return render(request,'index.html')

def control(request):
    obj={
        'state':'ON',
        'mode': 1,
        'battConnected' : "NO",
        'connect': 1,
    }
    return render(request,'control.html',obj)

def dashboard(request):
    dataSet = {
        'liveDataTime':[i for i in range(5)],
        'liveDataPower':[j for j in range(1,10,2)],
    }
    return render(request,'dashboard.html',dataSet)

def about(request):
    return render(request,'about.html')