import time

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

mc.postToChat("123")

time.sleep(5)

mc.postToChat("456")