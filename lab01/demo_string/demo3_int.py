from mcpi.minecraft import Minecraft
mc=Minecraft.create()
blockType=int(input("enter a block type:"))
x,y,z=mc.player.getPos()

mc.setBlock(x+1,y,z,blockType)