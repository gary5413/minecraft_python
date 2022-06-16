import time

from mcpi.minecraft import Minecraft
from time import sleep

mc=Minecraft.create()
x,y,z=mc.player.getTPos()

time.sleep(10)

x1,y1,z1=mc.player.getPos()

xDistance=x1-x
yDistance=y1-y
zDistance=z1-z

mc.postToChat("the player has moved:x:"+str(xDistance)+",y:"+str(yDistance)+",z:"+str(zDistance))

