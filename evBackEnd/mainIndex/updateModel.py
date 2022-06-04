from mainIndex.models import chargerState
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
