import paho.mqtt.client as mqtt
import os, urlparse, urllib

# Define event callbacks
def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    #Download the wav file via http
    audiofile = urllib.URLopener()
    audiofile.retrieve(str(msg.payload), "audio.wav")

    #In case aplay dose not play some wav files,we should convert it to pcm format.refer to https://ubuntuforums.org/showthread.php?t=1393045
    os.system("ffmpeg -y -i audio.wav final.wav")
    #Play the audio using aplay
    os.system("aplay -D plughw:1,0 final.wav")

#def on_publish(mosq, obj, mid):
#   print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
#mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://obbzesrv:ZFBjLQuS1h3A@m10.cloudmqtt.com:13198')
url = urlparse.urlparse(url_str)

# Connect
mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)

# Start subscribe, with QoS level 0
mqttc.subscribe("test", 0)

# Publish a message
#mqttc.publish("test", "my message")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
