# MQTT
IoT Security: Contains PA system project with MQTT implementation

Test files in home directory:
  -subcribe files: MQTT subscriber to test/LED topic, look for "engage" and "disengage" keywords
  -publish files : MQTT publisher to test/LED topic, sent "engage" or "disengage" keywords
  -broker: Mosquitto server
 
Stream folder:
  -contains Final.py: receives UDP packets and plays an audio stream; 
                      publishes "engage" keyword when stream begins;
                      publishes "disengage" keyword when stream ends/is interrupted
