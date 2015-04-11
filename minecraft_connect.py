import sys
sys.path.append('/opt/minecraft-pi/api/python/mcpi')
import minecraft

def game():
    mc = minecraft.Minecraft.create()
    return mc
