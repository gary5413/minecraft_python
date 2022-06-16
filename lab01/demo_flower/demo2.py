from mcpi.minecraft import Minecraft
from time import sleep

mc=Minecraft.create()

# x,y,z=mc.player.getPos()
# this_block=mc.getBlock(x,y,z)
# print(this_block)
#
# x,y,z=mc.player.getPos()
# block_beneath=mc.getBlock(x,y-1,z)
# print(block_beneath)
#
# while True:
#     x, y, z = mc.player.getPos()
#     block_beneath = mc.getBlock(x, y - 1, z)
#     print(block_beneath)

grass=2
flower=38

while True:
    x, y, z = mc.player.getPos()
    block_beneath = mc.getBlock(x, y - 1, z)
    print(block_beneath)

    if block_beneath==grass:
        mc.setBlock(x,y,z,flower)
        sleep(0.5)
    else:
        mc.setBlock(x,y-1,z,grass)