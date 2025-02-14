"""EE 250L Lab 04 
Chengzhong Luo
luoc@usc.edu"""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("luoc/ping")


    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("luoc/ping", on_message_from_ping)


def on_message_from_ping(client, userdata, message):

   num = int(message.payload.decode())
   print("ustom callback  - Received", num, "from", message.topic)

   num += 1
   client.publish("luoc/pong", num)
   print("Published", num, "to start_chain")
   



if __name__ == '__main__':
    #get IP address
    ip_address="68.181.32.115" 
    """your code here"""
    #create a client object
    client = mqtt.Client()
    
    client.on_message = on_message_from_ping
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    
    
    
    
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python. For example:
    
    `client.connect("eclipse.usc.edu", 11000, 60)` 
    
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    #client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.connect(host="172.20.10.9", port=11000, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_forever()
    








        
