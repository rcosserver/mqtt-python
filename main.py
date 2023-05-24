import paho.mqtt.client as mqtt
import os, urllib.parse

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    #print("rc: " + str(rc))
    print()
def on_message(client, obj, msg):
    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print((str(msg.payload)[2:7]))
def on_publish(client, obj, mid):
    #print("mid: " + str(mid))
    print()
def on_subscribe(client, obj, mid, granted_qos):
    #print("Subscribed: " + str(mid) + " " + str(granted_qos))
    print()
#def on_log(client, obj, level, string):
#    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
#mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
#mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
#url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')
#url = urllib.parse.urlparse(url_str)
topic_temp = 'esp32/bme280/temperature'
topic_hym = 'esp32/bme280/humidity'
topic_pres = 'esp32/bme280/pressure'

# Connect
mqttc.username_pw_set('___________', '_____________')
mqttc.connect("________", 7672)

# Start subscribe, with QoS level 0
temp = mqttc.subscribe(topic_temp, 0)
#hymi = mqttc.subscribe(topic_hym, 0)
#pres = mqttc.subscribe(topic_pres, 0)

# Publish a message
#mqttc.publish("esp32/IRSend/", "ON")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
#text = rc



