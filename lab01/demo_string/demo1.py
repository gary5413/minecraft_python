from mcpi.minecraft import Minecraft
mc=Minecraft.create()
message="預設訊息"
# message=input("this is the default message")

mc.postToChat(message)
