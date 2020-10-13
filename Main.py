#
# Copyright (C) 2020 vExo307. All rights reserved.
#
# You may distribute and edit this code freely, so long as you do not sell it.
#
import datetime
import json
import os
import os.path
import secrets
import requests
import asyncio
import time
from pypresence import Presence
from datetime import datetime

currentdirectory = os.path.dirname(os.path.abspath(__file__))
config = os.path.join(currentdirectory, 'config.json')

with open(config, 'r+') as f:
  data = json.load(f)

def getStatus():
    xuid = data["xuid"]
    r = requests.get(url=f"https://xapi.us/v2/{xuid}/presence", headers={"X-AUTH": data["liveapi"]})
    return r.text

currentgameid = 0
timeelapsed = 0

RPC = Presence(data["clientid"],pipe=data["client"])
RPC.connect()
while True:
    status = json.loads(getStatus())
    state = status["state"]
    if(state == "Offline"):
        continue
    device = status["devices"][0]["type"]
    game = status["devices"][0]["titles"][0]["name"]
    gameid = status["devices"][0]["titles"][0]["id"]
    gamestate = status["devices"][0]["titles"][0]["state"]
    if(gameid != currentgameid):
        timeelapsed = int(time.time())
        currentgameid = gameid
    RPC.update(state=f"Playing {game}", details=f"{gamestate} | Using {device}", start=timeelapsed)
    time.sleep(data["updatedelay"])



