from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getPos()
block=24
for i in range(10):
    mc.setBlocks(x-i,y-i,z-i,x+i,y-i,z+i,block)