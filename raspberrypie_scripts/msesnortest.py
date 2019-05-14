import RPi.GPIO as GPIO
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time


sensor = 16


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)


clientId = "myClientID"
thingEndpoint = ''
certificatePath = ''
privateKeyPath = ''
rooCACertPath = ''
print "before setup1 ..."

myMQTTClient = AWSIoTMQTTClient(clientId)
myMQTTClient.configureEndpoint(thingEndpoint, 8883)
myMQTTClient.configureCredentials(rooCACertPath, privateKeyPath, certificatePath)

myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish q  myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
print "before connection..."

myMQTTClient.connect()

print "connected"

myTopic = "sendButtonClick"
message = {}
message['text'] = "This is message"
message['type'] = "This is message type"
messageJson = json.dumps(message)


print "Initialzing PIR Sensor......"
time.sleep(12)
print "PIR Ready..."
print " "


try: 
   while True:
      if GPIO.input(sensor):
          print "Motion Detected"
          myMQTTClient.publish(myTopic, messageJson, 0)
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          print "No motion"

except KeyboardInterrupt:
    GPIO.cleanup()


