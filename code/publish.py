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
credential = sys.argv[1]
message = sys.argv[2]
clientID = sys.argv[3]

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL', credential)
url = urlparse.urlparse(url_str)

# Connect
mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)

# Publish a message
mqttc.publish(clientID, message)

#disconnect this client
mqttc.disconnect();
