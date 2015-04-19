import sys
import minecraft_connect

game = minecraft_connect.game()
player = game.player

x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]

x = int(x)
y = int(y)
z = int(z)

player.setPos(x, z, y)

