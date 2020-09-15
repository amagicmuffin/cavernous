import pygame
from config import *


crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveUp()
            if event.key == pygame.K_a:
                moveLeft()
            if event.key == pygame.K_s:
                moveDown()
            if event.key == pygame.K_d:
                moveRight()



        #print(event)
    
    #renderImg(dotImg,50,50)
    
    #pygame.display.update() #only update parts of thing
    #clock.tick(60) this piece of code crashes the thing after three or so seconds :)
exit()
