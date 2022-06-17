from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create()
# x, y, z = mc.player.getPos()
# mc.setBlocks(x,y,z,x+2,y,z+2,1)
start=mc.player.getTilePos()

final=mc.player.setTilePos(start.x+100,start.y,start.z)

def make_east():
    x, y, z = mc.player.getPos()
    mc.setBlock(x+1,y-1,z,random.randint(1,100))
    mc.setBlock(x+2,y-1,z,random.randint(1,100))
    mc.setBlock(x+3,y-1,z,random.randint(1,100))
    print("east")

def make_west():
    x, y, z = mc.player.getPos()
    mc.setBlock(x-1,y-1,z,random.randint(1,100))
    mc.setBlock(x-2,y-1,z,random.randint(1,100))
    mc.setBlock(x-3,y-1,z,random.randint(1,100))
    print("west")

def make_south():
    x, y, z = mc.player.getPos()
    mc.setBlock(x,y-1,z+1,random.randint(1,100))
    mc.setBlock(x,y-1,z+2,random.randint(1,100))
    mc.setBlock(x,y-1,z+3,random.randint(1,100))
    print("south")

def make_north():
    x, y, z = mc.player.getPos()
    mc.setBlock(x,y-1,z-1,random.randint(1,100))
    mc.setBlock(x,y-1,z-2,random.randint(1,100))
    mc.setBlock(x,y-1,z-3,random.randint(1,100))
    print("north")

while True:
    time.sleep(3)
    go=random.randint(1,4)
    if go==1:
        make_east()
    elif go==2:
        make_west()
    elif go==3:
        make_north()
    elif go==4:
        make_south()



# while True:
#     x, y, z = mc.player.getPos()
#     time.sleep(5)
#     x=x+random.randint(-3,3)
#     z=z+random.randint(-3,3)
#     mc.setBlock(x,y-1,z,1)
#     r=random.randint(-2,2)
#     mc.setBlock(x+r,y-1,z+r,2)
#     mc.setBlock(x+r,y-1,z+r,3)
#     mc.setBlock(x + r, y - 1, z + r, 3)
