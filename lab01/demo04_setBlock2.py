from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
pos=mc.player.getPos()

mc.setBlock(pos.x+2,pos.y,pos.z,block.STONE.id)
