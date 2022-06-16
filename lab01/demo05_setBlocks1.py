from mcpi.minecraft import Minecraft
from mcpi import block

mc=Minecraft.create()
pos=mc.player.getPos()
# mc.setBlocks(pos.x+1,pos.y+1,pos.z+1,pos.x+10,pos.y+10,pos.z+10,1)


# mc.setBlocks(pos.x,pos.y,pos.z,pos.x+2,pos.y,pos.z,1)
mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y,pos.z+2,1)