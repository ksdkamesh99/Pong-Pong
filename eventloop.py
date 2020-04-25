import pygame as pg
from pygame.locals import *
import sys
#color
red=(255,0,0)
#initialise game
pg.init()
#create a window screen
window=pg.display.set_mode((1000,600))
pg.display.set_caption("Snake Game")
#creating a surface
screen=pg.display.get_surface()
screen.fill(red)
pg.display.set_caption("Slither-Eat")
pg.display.flip()
while True:
    for event in pg.event.get():
        print(event)
        if event.type== QUIT:
            pg.quit()
            sys.exit()
        
        pg.display.update()

