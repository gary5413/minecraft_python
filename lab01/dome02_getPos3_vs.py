from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getPos()

type(x)
print(x,y,z)

x1,y1,z1=mc.player.getTilePos()

type(x1)
print(x1,y1,z1)