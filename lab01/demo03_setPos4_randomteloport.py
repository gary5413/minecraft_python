import time

from mcpi.minecraft import Minecraft
import random

mc=Minecraft.create()
x,y,z=mc.player.getPos()
while True:
    x=x+random.randint(-10,10)
    y=y + random.randint(-10, 10)
    z=z + random.randint(-10, 10)

    mc.player.setPos(x,y,z)
    time.sleep(2)

