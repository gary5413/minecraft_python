from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlocks(x,y-1,z,x+2,y,z+2,1)

while True:
    x, y, z = mc.player.getPos()
    time.sleep(5)
    x=x+random.randint(-3,3)
    z=z+random.randint(-3,3)
    mc.setBlock(x,y-1,z,1)
    r=random.randint(-2,2)
    mc.setBlock(x+r,y-1,z+r,2)
    mc.setBlock(x+r,y-1,z+r,3)
    mc.setBlock(x + r, y - 1, z + r, 3)
