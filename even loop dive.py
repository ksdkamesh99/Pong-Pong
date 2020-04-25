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
global ctx,cty,screen

screen=0
screen=pg.display.get_surface()
screen.fill(red)
pg.display.set_caption("Slither-Eat")
pg.display.flip()
ctx=100
cty=100

while True:
    
    for event in pg.event.get():
        print(event)
        if event.type== QUIT:
            pg.quit()
            sys.exit()
        else:
            if event.type==KEYDOWN:
                print("hi")
                if event.key==K_s:
                    print("down")
                    cty=cty+2
                elif event.key==K_w:
                    print("up")
                    cty=cty-2
                elif event.key==K_a:
                    print("left")
                    ctx=ctx-2
                elif event.key==K_d:
                    print("right")
                    ctx=ctx+2
        print(ctx)
        print(cty)
        screen.fill((0,0,0))
        pg.draw.rect(screen,(255,0,0),(ctx,cty,50,10))
        pg.display.update()

