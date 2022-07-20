from operator import mod
from . import mqtt
import datetime
from random import Random, randint, random
from statistics import mode
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mainIndex.models import chargerState, pConsumptionData
# Create your views here.


def index(request):
    return render(request, 'index.html')


def control(request):
    obj = chargerState.objects.get(id=1)
    objPara = {
        'chargerState': obj.charger_state,
        'chargerMode': obj.charger_mode,
        'evConnectState': obj.ev_connect_state,
        'time': obj.update_time,
        'date': obj.update_date,
    }
    try:
        mode = request.GET.get('Mode')
        if mode == "CNow":
            mqtt.client.publish("ev/charger/set/mode", "1", 0, False)

        elif mode == "1LHR":
            mqtt.client.publish("ev/charger/set/mode", "2", 0, False)

        elif mode == "2V2H":
            mqtt.client.publish("ev/charger/set/mode", "3", 0, False)

        elif mode == "3PV":
            mqtt.client.publish("ev/charger/set/mode", "4", 0, False)

        elif mode == "off":
            mqtt.client.publish("ev/charger/set/mode", "0", 0, False)
        
        else:
            print("Invalid Control Input")

    except:
        print('Exception occured')

    return render(request, 'control.html', objPara)


def dashboard(request):
    objLastRow = pConsumptionData.objects.last()
    today = datetime.datetime.now()
    objTodayData = pConsumptionData.objects.filter(
        update_data__month=today.month)

    pConsumByHome = 0
    pBatteryFromPv = 0
    pBatteryFromUtil = 0
    for data in objTodayData:
        pConsumByHome = pConsumByHome + (data.pow_cnsmp_frm_grid)
        pBatteryFromPv = pBatteryFromPv + (data.pow_cnsmp_frm_pv)
        pBatteryFromUtil = pBatteryFromUtil + (data.ev_batt_power_cnsmp)

    pBatteryFromUtil = pBatteryFromUtil - pBatteryFromPv

    last_ten = pConsumptionData.objects.all().order_by('id')[:20]
    # last_ten_in_ascending_order = reversed(last_ten)
    time = []
    homePower = []
    batteryPower = []
    for data in last_ten:
        time.append(int(data.update_time.strftime("%M")))
        homePower.append(data.pow_cnsmp_frm_grid)
        batteryPower.append(data.ev_batt_power_cnsmp)
    dataSet = {
        'gVolts': objLastRow.grid_voltage,
        'sVolts': objLastRow.solar_pv_voltage,
        'bVolts': objLastRow.ev_batt_voltage,
        'time': objLastRow.update_time,
        # Power Consumption by EV Battery From Utility.
        'pBatryFrmUtil': pBatteryFromUtil,
        # Power Consumption by EV Battery From PV Array.
        'pBatryFrmPv': pBatteryFromPv,
        # Power Consumption by Home form Utility supply.
        'pConsumByHome': pConsumByHome,
        # Power Consumption by EV Battery from Utility Supply.
        'pConsumByBatt': pBatteryFromUtil,
        'liveTime': time,
        'liveHomePower': homePower,
        'libeBattPower': batteryPower,
    }
    return render(request, 'dashboard.html', dataSet)


def about(request):
    return render(request, 'about.html')
