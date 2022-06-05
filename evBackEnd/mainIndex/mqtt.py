import paho.mqtt.client as mqtt
from mainIndex.updateModel import updateModel

HOST_IP = '127.0.0.1'
HOST_PORT = 1883
KEEPALIVE = 60
client = mqtt.Client()


def on_connect(client, userdata, flags, rc):
    client.subscribe("ev/charger/get/#")


def on_message(client, userdata, msg):
    print(msg.topic)
    if msg.topic    == "ev/charger/get/modeUpdate/":
        updateModel.updateChargerState(msg.payload)
        print(msg.payload)
    elif msg.topic  == "ev/charger/get/ConsumptionData/":
        updateModel.updateConsumptionData(msg.payload)
    elif msg.topic  == "ev/charger/get/grid/cmd/":
        pass
    else:
        print("Invalid Topic")


client.on_connect = on_connect
client.on_message = on_message
client.connect(HOST_IP, HOST_PORT, KEEPALIVE)


client.loop_start()
