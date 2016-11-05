'''
Created on Oct 2, 2016

@author: Jorge Pantoja
'''

# [Credentials]
# username = sebastian.viteri@bproces.com
# password = limpiezaexcelente
# 
# [PowerTrack]
# url = https://gnip-stream.twitter.com/stream/powertrack/accounts/Bproces/publishers/twitter/prod.json
# rules_url = https://gnip-stream.twitter.com/stream/powertrack/accounts/Bproces/publishers/twitter/rules.json

#!/usr/bin/env python
import time
from gnippy import PowerTrackClient

# Define a callback
def callback(activity):
    print (activity)

# Create the client
client = PowerTrackClient(callback, url="https://gnip-stream.twitter.com/stream/powertrack/accounts/Bproces/publishers/twitter/prod.json", auth=("sebastian.viteri@bproces.com", "limpiezaexcelente"))
client.connect()

# Wait for 2 minutes and then disconnect
time.sleep(120)
client.disconnect()