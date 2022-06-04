from mainIndex.models import chargerState, pConsumptionData
import json

class updateModel:
    def updateChargerState(recivedJson):
        jsonData = json.loads(recivedJson)
        modelObj = chargerState.objects.get(id=1)
        modelObj.charger_state      = jsonData["chargerState"]
        modelObj.charger_mode       = jsonData["chargerMode"]
        modelObj.ev_connect_state   = jsonData['evConnectState']
        modelObj.update_time        = jsonData['time']
        modelObj.update_date        = jsonData['date']
        modelObj.save()

    def updateConsumptionData(recivedJson):
        jsonData = json.loads(recivedJson)
        update = pConsumptionData(
            update_time          =   jsonData["time"],
            update_data          =   jsonData["date"],
            grid_voltage         =   jsonData["gridVoltage"],
            pow_cnsmp_frm_grid   =   jsonData["powerConspFromGrid"],
            solar_pv_voltage     =   jsonData["solarPvVoltage"],
            pow_cnsmp_frm_pv     =   jsonData["powerConspFromPv"],
            ev_batt_voltage      =   jsonData["evBattVoltage"],
            ev_batt_power_cnsmp  =   jsonData['evBattPowerConsmp']
            )
        update.save()