from mcpi.minecraft import Minecraft
from time import sleep

mc=Minecraft.create()
x,y,z=mc.player.getPos()

while True:
    mc.setBlock(x+1,y,z,103)
    y=y+1
    sleep(1)
