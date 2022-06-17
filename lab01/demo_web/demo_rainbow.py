from mcpi.minecraft import Minecraft
from mcpi import block
import time,math

mc=Minecraft.create()
mc.postToChat("Rainbow")
pos=mc.player.getTilePos()
# red ,orange ,yellow ,green,blue,indigo,violet
rainbow=[14,1,4,13,11,10,2]
radius=30
# for i in range(16):
#     mc.setBlock(x,y+2,z,block.WOOD.id,i)

for angle in range(360):
    for i in range(len(rainbow)):
        x=pos.x+((radius-i)* math.cos(angle * (math.pi/180)))
        y=pos.y+((radius-i)* math.sin(angle * (math.pi/180)))
        mc.setBlock(x,y,pos.z,block.WOOL.id,rainbow[i])
        time.sleep(0.1)