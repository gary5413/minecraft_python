from mcpi.minecraft import Minecraft

mc=Minecraft.create()

# pos=mc.player.getPos()
pos=mc.player.getTilePos()
mc.postToChat(str(pos.x)+","+str(pos.y)+","+str(pos.z))