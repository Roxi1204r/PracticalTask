import time
import datetime
import json
import string
import random
from random import seed
from random import randint
import paho.mqtt.publish as publicare
MQTT_HOST = 'mqtt.beia-telemetrie.ro'
MQTT_TOPIC = 'training/device/Roxana-Roscaneanu'
logfile="Roxana-Roscaneanu.txt"
def local_save(data):
    file=open(logfile, "a+")
    file.write(data+"\r\n")
    file.close()
Gas=0
vect1=[]
vect2=[]
Atentionare=0
seed(1)
value1=0
value2=0
for _ in range(100):
    value=randint(0,100)
    vect1.append(value)
for _ in range(100):
    value=randint(0,1)
    vect2.append(value)
while True:
    value1=random.choice(vect1)
    value2=random.choice(vect2)
    if value1>50:
        Gas=1
    elif value1<=50:
        Gas=0
    if value2==0:
        Atentionare=0
    elif value2==1:
        Atentionare=1
    payload_dict={"value1":Gas,
                  "value2":Atentionare}
    print(json.dumps(payload_dict))
    message="Gas detected "+str(Gas)+", Warning "+str(Atentionare)
    try:
        publicare.single(MQTT_TOPIC,qos = 1,hostname = MQTT_HOST,payload = json.dumps(payload_dict))
        local_save(message)
    except:
        pass
    time.sleep(60)