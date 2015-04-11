import sys
import minecraft_connect

game = minecraft_connect.game()
while True:
    line = sys.stdin.readline().strip()
    game.postToChat(line)
