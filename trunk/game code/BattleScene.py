import pygame, sys,os
from Scene import Scene
from pygame.locals import * 

class BattleScene(Scene):

    def __init__(self):
    
        global screen,screenbackground
        screen = pygame.display.get_surface() 
        screenbackground = pygame.Surface(pygame.display.get_surface().get_size())
        screenbackground.fill((0,0,0))


       
        global background,view
        
        background = pygame.Surface((1042,1024))
        
        background = background.convert()
        backimg = os.path.join("images","background2.png")
        backimage = pygame.image.load(backimg)
        #background.fill((51, 153, 0))
        background.blit(backimage,(0,0))

        
