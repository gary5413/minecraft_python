import math
import time

from mcpi.minecraft import Minecraft
from mcpi import block
import datetime

mc=Minecraft.create()
pos=mc.player.getTilePos()
while True:
    now=datetime.datetime.now()
    # mc.postToChat(now)
    radius=30
    angle=90
    for angle in range(360):
        x=pos.x+radius*math.cos(angle*math.pi/180)
        y =pos.y+ radius * math.sin(angle * math.pi / 180)
        mc.setBlock(x,y,pos.z,block.WOOD.id,1)


    hour=now.hour
    min=now.min
    sec=now.second
    # time.sleep(1)