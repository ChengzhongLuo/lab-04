"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))


if __name__ == '__main__':
    #get IP address
    ip_address=68.181.32.115 
    """your code here"""
    #create a client object
    client = mqtt.Client()
    
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

    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1)

    while True:
        #replace user with your USC username in all subscriptions
        client.publish("luoc/ipinfo", f"{ip_address}")
        print("Publishing ip address")
        time.sleep(4)

        #get date and time 
        current_datetime = datetime.datetime.now()
        # Get the year, month, and day
        year = current_datetime.year
        month = current_datetime.month
        day = current_datetime.day

        # Get the hour, minute, and second
        hour = current_datetime.hour
        minute = current_datetime.minute
        second = current_datetime.second
        """your code here"""
        #publish date and time in their own topics
        """your code here"""
        client.publish("luoc/datetime", f"{ip_address}")
        print("Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(4)













