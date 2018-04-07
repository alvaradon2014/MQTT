## -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client("python_pub")
mqttc.connect("192.168.1.14", 1883)
mqttc.publish("test/led", "ENGAGE")
time.sleep(1)
#mqttc.loop(2) #timeout = 2s
mqttc.publish("test/led", "DISENGAGE")
mqttc.disconnect();
