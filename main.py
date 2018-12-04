# System imports
import pygame as pg
import sys

# Engine imports
from game import Game

g = Game()
g.show_start_screen()

while True:
    g.new()
    g.run()
    g.show_go_screen()
