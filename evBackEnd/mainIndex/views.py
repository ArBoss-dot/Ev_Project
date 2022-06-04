from . import mqtt
from random import Random, randint, random
from statistics import mode
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mainIndex.models import chargerState
# Create your views here.

def index(request):
    return render(request,'index.html')

def control(request):
    obj = chargerState.objects.get(id=1)
    objPara={
        'chargerState': obj.charger_state,
        'chargerMode': obj.charger_mode,
        'evConnectState' :obj.ev_connect_state,
    }
    try:
        mode = request.GET.get('Mode')
        if mode == "CNow":
            mqtt.client.publish("ev/charger/modeSet","1",0,False)
            
        elif mode == "1LHR":
            mqtt.client.publish("ev/charger/modeSet","2",0,False)
            
        elif mode == "2V2H":
            mqtt.client.publish("ev/charger/modeSet","3",0,False)
            
        elif mode == "3PV":
            mqtt.client.publish("ev/charger/modeSet","4",0,False) 
        else:
            pass

    except:
        print('Exception occured')

    return render(request,'control.html',objPara)

def dashboard(request):
    dataSet = {
        'liveDataTime':[i for i in range(5)],
        'liveDataPower':[j for j in range(1,10,2)],
    }
    return render(request,'dashboard.html',dataSet)

def about(request):
    return render(request,'about.html')