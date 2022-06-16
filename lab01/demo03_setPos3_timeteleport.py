import time

from mcpi.minecraft import Minecraft
from time import sleep

mc=Minecraft.create()

mc.player.setPos(100,100,100)

time.sleep(10)

mc.player.setPos(0,0,0)