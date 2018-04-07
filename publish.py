# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.connect("192.168.1.103", 1883)
mqttc.publish("hello/world", "Hello, World!")
# mqttc.loop(2) #timeout = 2s
mqttc.disconnect();
