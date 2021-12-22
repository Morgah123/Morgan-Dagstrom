from sense_hat import SenseHat #import modul för sensehat
import time #import time
import paho.mqtt.client as mqtt #importeras för att mqtt ska fungera
import json #För att vi ska kunna läsa in dict till thingsboard
import math

sense = senseHat()

iot_hub = "thingsboard.port0.org" #Skriv vilken hub
port = 1883 #port 1883
username = "S3uMRKd4QtsXj30BU6Lv" #Skriv access token
password ="" #lämnas tom
topic = "v1/devices/me/telemetry" #skriv in sökväg ish, standard /v1/devices/me/telemetry

client = mqtt.Client()
client.username_pw_set(username)
client.connect(iot_hub,port)
print("connection success")

try:
        while True:
                lista = []
                for i in range(10): # kör for loop i 5 sekunder
                        accx, accy, accz = sense.get_accelerometer_raw().values() #get gkraften på de olika axlarna
                        acc = math.sqrt((accx * accx) + (accy * accy) + (accz * accz)) #Ger oss normen av vektor x y z
                        lista.append(acc)
                        time.sleep(0.5) #vänta 0.5 s
                skakningar = max[lista] - min[lista]
                timestamp_ms = time.time() * 1000 #ger oss rätt tis i ms  
                payload = {'ts': timestamp_ms , 'values':{'temperatur': sense.get_temperature(), 'skakningar' : skakningar * 10}} #Här är vår dict som innehåller rätt data
                c = payload['values']['temperatur'] #temp
                s = payload['values']['skakningar'] #skakningar
                print(c, s) #printar ut temp och antal skakningar
                client.publish(topic,json.dumps(payload),1) #Laddar upp dict på thingsboard via json
except KeyboardInterrupt: #ctrl c för att komma ut loop
        print('\nslut')