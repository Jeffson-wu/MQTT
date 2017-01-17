import paho.mqtt.client as mqtt
import os, urlparse, sys

# Define event callbacks
def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_log(mosq, obj, level, string):
    print(string)

#Phase the command line argument
param_1 = sys.argv[1]
param_2 = sys.argv[2]

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL', param_1)#'mqtt://obbzesrv:ZFBjLQuS1h3A@m10.cloudmqtt.com:13198')
url = urlparse.urlparse(url_str)

# Connect
mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)

# Publish a message
mqttc.publish("test", param_2)#"http://www.thewavsite.com/Birthday/bday02.wav")

#disconnect this client
mqttc.disconnect();
