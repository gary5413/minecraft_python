from mcpi.minecraft import Minecraft

tnt=46
mc=Minecraft.create()
x,y,z=mc.player.getPos()
# mc.setBlock(x,y,z,tnt)
# mc.setBlock(x,y,z,tnt,1)

mc.setBlocks(x+1,y+1,z+1,x+11,y+11,z+11,tnt,1)
