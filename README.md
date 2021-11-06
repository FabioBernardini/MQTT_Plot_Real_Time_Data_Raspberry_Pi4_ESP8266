# MQTT_Plot_Real_Time_Data_Raspberry_Pi4_ESP8266-
In this repository, the code for implementing a MQTT communication between an ESP8266 and a Raspberry Pi 4 is represented. In particular, the ESP8266 sends temperature and humidity values coming from a DHT11 sensor. The values are sent to a broker MQTT and then visualized in real-time with Raspberry Pi 4 

In this case, the ESP8266 will be the publisher, while the Raspberry Pi 4 will be the subscriber and it will represent the sensor data.

The script .py holds the Raspberry Pi 4 code using to subscribe to the particular Topic and then to represent the sensor data.

The script .ino holds the code to compile and to load on the ESP8266. This code allows to receive the data from the sensor and then to publish them on the topic.
