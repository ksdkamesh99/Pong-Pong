import pygame as pg
import sys
import random
#initialising pygame
pg.init()
#colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
#creating menu
title = pg.image.load("Pong-pong.png")
title = pg.transform.scale(title, (500, 81 * 2))

#creating a paddle:-
def paddle(screen,x,y):
    pg.draw.rect(screen,red,(x,y,50,10))
# creating a window
window=pg.display.set_mode((800,700))
pg.display.set_caption("POng poNG")
#creating surface
screen=pg.display.get_surface()
screen.fill(black)
pg.display.flip()
#initialising coordinates
pad_x=100
pad_y=690
pad_change_x=0
pad_change_y=0
ball_x=350
ball_y=200
ball_change_x=3
ball_change_y=3
clock=pg.time.Clock()
scoreA=0
scoreB=0
#Event Loop
while True:
    for event in pg.event.get():
        pad_change_x=0
        pad_change_y=0

        if event.type==pg.QUIT:
            pg.quit()
            sys.exit(0)
        else:
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_RIGHT:
                    pad_change_x=100
                elif event.key==pg.K_LEFT:
                    pad_change_x=-100
                elif event.key==pg.K_DOWN or event.key==pg.K_UP:
                    pad_change_y=0
        pad_x=pad_x+pad_change_x
        pad_y=pad_y+pad_change_y
        #setting linits to paddle
        if pad_x<0:
            pad_x=0
        if pad_x>650:
            pad_x=650
    ball_x+=ball_change_x
    ball_y+=ball_change_y
    u1=random.randint(0,350)
    u2=random.randint(400,700)
    if ball_x<0:
        ball_x=u1
        ball_change_x=ball_change_x*-1
    elif ball_x>700:
        ball_x=u2
        ball_change_x=ball_change_x*-1
    elif ball_y<0:
        ball_y=u1
        ball_change_y=ball_change_y*-1
    elif (ball_x>pad_x and ball_x<=pad_x+50) and (ball_y==778):
        scoreB=scoreB+1
        print(scoreB)
        ball_change_y=ball_change_y*-1
    elif ball_y>700:
        ball_y=u2
        ball_change_y=ball_change_y*-1
        scoreA=scoreA+1
        print(scoreA)
    screen.fill(black)

    pg.draw.rect(screen,white,(ball_x,ball_y,10,10))
    paddle(screen,pad_x,pad_y)
    font = pg.font.Font(None,40)
    text = font.render("Computer Score is "+str(scoreA), 1, white)
    screen.blit(text, (10,10))
    text = font.render("Your Score is "+str(scoreB), 1, white)
    screen.blit(text, (10,50))

    
    pg.display.update()
    clock.tick(60)

