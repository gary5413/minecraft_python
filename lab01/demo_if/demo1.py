from mcpi.minecraft import Minecraft
mc=Minecraft.create()

create=input("Create a watermelon Y/N:")
x, y, z = mc.player.getPos()

if create =="Y":
    mc.setBlocks(x+1,y+1,z+1,x+4,y+4,z+4,103)
    mc.postToChat("西瓜")
else:
    mc.setBlocks(x + 1, y + 1, z + 1, x + 4, y + 4, z + 4, 46)
    mc.postToChat("TNT")