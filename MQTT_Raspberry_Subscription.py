"""
Author: Fabio Bernardini

In this script there is the subscription to the MQTT topic by the Raspberry Pi
to receive the sensor data coming from the ESP8266.
The data are plotted to see their values in real-time

"""
# importiamo la libreria paho
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import json

# Creiamo le funzione di callback per il subscriber e per ricevere i mesaggi.
def on_connect(client, userdata, flags, rc):
    print("Connessione con il broker con codice: "+str(rc))

    """
    Effettuiamo la subscribe al topic 
    """
    client.subscribe("ESP8266/dataSensor")

def on_message(client, userdata, msg):

    print("ho ricevuto un messaggio con il seguente topic: "+msg.topic+" e il seguente contenuto: "+str(msg.payload, "utf-8"))
    
    if msg.payload != None:
        msg_payload = json.loads(msg.payload.decode())
        temp = float(msg_payload["parameters"]["temp"])
        hum = float(msg_payload["parameters"]["humidity"])
        
        x.append(temp)
        y.append(hum)

        fig, (ax1, ax2) = plt.subplots(2, 1)
        ax1.plot(x,label='temp')
        ax1.set_xlabel('Time (s)')  
        ax1.set_ylabel('°C')  
        ax1.title.set_text("Temperature")  
        ax2.plot(y,label='hum')
        ax2.set_xlabel('Time (s)')  
        ax2.set_ylabel('%')  
        ax2.title.set_text("Humidity")  
        plt.show()


client = mqtt.Client()

x = list()
y = list()

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883, 60)

client.loop_forever()
