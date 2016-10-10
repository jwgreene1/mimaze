#!/usr/bin/env python

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import datetime
import math


#mid point circle algorithm
def createTunnelSegment(mc, x0, y0, z, radius, blockType, torch):

    blockType2 = block.AIR
    blockType3 = block.AIR
    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius
    x = 0
    y = radius
    sleep = 0 
    sleep2 = 0 
    sideSlots = round(radius * .25)
    slotFilled = dict()

    #print "Creating Tunnel, Radius:",radius,", sideSlots:",sideSlots,", torch: ",torch
    time.sleep(sleep)

    #print "Set the top block"
    mc.setBlock(x0, y0 + radius, z, blockType)
    time.sleep(sleep)
    #print "Set the bottom block"
    mc.setBlock(x0, y0 - radius, z, blockType)
    time.sleep(sleep)
    #print "Set the left block"
    mc.setBlock(x0 + radius, y0, z, blockType)
    if(torch):
        #print "Setting a torch, x:",x0 + radius,", y:",y0,", z:",z
        mc.setBlock(x0 + radius + 1, y0, z, blockType)
        mc.setBlock(x0 + radius, y0, z, block.TORCH, 1)
        print "Left Torch block data: ", mc.getBlockWithData(x0 + radius , y0, z)
    time.sleep(sleep)
    #print "Set the right block"
    mc.setBlock(x0 - radius, y0, z, blockType)
    if(torch):
        #print "Setting a torch, x:",x0 - radius,", y:",y0,", z:",z
        mc.setBlock(x0 - radius - 1, y0, z, blockType)
        mc.setBlock(x0 - radius, y0, z, block.TORCH, 2)
        print "Right Torch block data: ", mc.getBlockWithData(x0 - radius , y0, z)
    time.sleep(sleep)

    # Fill the center line
    #print "Fill Circle Center line verticle"
    y1 = y0 - y + 1
    y2 = y0 + y
    while y1 < y2:
        mc.setBlock(x0, y1, z, blockType2)
        y1 += 1
        time.sleep(sleep2)

    counter = 0

    while x < y:
        if f >= 0:
            y -= 1
            ddf_y += 2
            f += ddf_y
        x += 1
        ddf_x += 2
        f += ddf_x   

        counter += 1

        #print "Set the blocks to the right and left of the top blocks"
        mc.setBlock(x0 + x, y0 + y, z, blockType)
        time.sleep(sleep)
        mc.setBlock(x0 - x, y0 + y, z, blockType)
        time.sleep(sleep)

        #print "Set the blocks to the right and left of the bottom blocks"
        mc.setBlock(x0 + x, y0 - y, z, blockType)
        time.sleep(sleep)
        mc.setBlock(x0 - x, y0 - y, z, blockType)
        time.sleep(sleep)
        if(x < radius):
            #print "Fill Circle Loop 2"
            y1 = y0 - y + 1
            y2 = y0 + y
            while y1 < y2:
                mc.setBlock(x0 + x, y1, z, blockType2)
                mc.setBlock(x0 - x, y1, z, blockType2)
                y1 += 1
                time.sleep(sleep2)

        #print "Set the blocks above the side blocks"
        mc.setBlock(x0 + y, y0 + x, z, blockType)
        time.sleep(sleep)
        mc.setBlock(x0 - y, y0 + x, z, blockType)
        time.sleep(sleep)

        #print "Set the blocks below the side blocks"
        mc.setBlock(x0 + y, y0 - x, z, blockType)
        time.sleep(sleep)
        mc.setBlock(x0 - y, y0 - x, z, blockType)
        time.sleep(sleep)
        #print "y:",y
        if(radius > y > (radius - sideSlots)):
            if((x0 + y) in slotFilled):
                #print "slot:",(x0 + y)," is filled already, skip"
                a = 1
            else:
                y1 = y0 - x + 1
                y2 = y0 + x
                #print "Fill the side slot blocks"
                while y1 < y2:
                    mc.setBlock(x0 + y, y1, z, blockType3)
                    mc.setBlock(x0 - y, y1, z, blockType3)
                    y1 += 1
                    time.sleep(sleep2)

                # Set the slot hash so you don't fill this slot again
                slotFilled[(x0 +y)] = 1

#find point on circle
def findPointOnCircle(cx, cy, radius, angle):
    x = cx + math.sin(math.radians(angle)) * radius
    y = cy + math.cos(math.radians(angle)) * radius
    return((int(x + 0.5),int(y + 0.5)))

# Create a tunnel
def createTunnel():

    mc = minecraft.Minecraft.create()

    # Find your position
    position = mc.player.getPos()

    # Now put the tunnel 10 blocks ahead on the z axis, y + radius
    radius = 3
    x = position.x
    y = position.y + radius - 1
    z = position.z + 1

    mc.postToChat("Creating a tunnel, center is: x=%s y=%s z=%s" % (int(x), int(y), int(z)))
    print "Creating a tunnel, center is: x=%s y=%s z=%s" % (int(x), int(y), int(z))

    length = 0

    while(length < 50):

        length += 1
        torch = 0

        if(int(round(z)) % 5 == 0):
            torch = 1

        tunnelCenter = minecraft.Vec3(x, y, z)

        #z -= 1 
        z += 1 
        #radius += 1 

        blockType = block.OBSIDIAN
        createTunnelSegment(mc, tunnelCenter.x, tunnelCenter.y, tunnelCenter.z, radius, blockType, torch)


if __name__ == "__main__":
    sys.exit(createTunnel())
