import pygame as pg
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
    print("My first game program")
    pass