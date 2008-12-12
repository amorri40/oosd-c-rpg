import pygame, sys,os
from pygame.locals import * 
from MainScene import MainScene
from splashscreen import Splashscreen
from HouseScene import HouseScene
from menuScreen import menuScreen
 
pygame.init()
running = True
 
window = pygame.display.set_mode((300, 300)) 
pygame.display.set_caption('RPG game coursework') 

pygame.display.flip() 
 
ms = menuScreen()





class Game:
    def __init__(self,scene):
        self.mainscene=MainScene()
        
        self.currentScene = self.mainscene
        
        
        
        
        #splash = Splashscreen()
    def run(self):
         while running: 
            self.input(pygame.event.get())
            pygame.display.flip() 
            self.currentScene.draw()
            
    def gotoHouse(self):
        self.currentScene=HouseScene()
    def gotoMain(self):
        self.currentScene=MainScene()    
        
    def input(self,events): 
     for event in events: 
      if event.type == QUIT:
         pygame.display.quit()
         print "quit"
      else: 
         self.currentScene.event(events) 

g = Game(ms)
g.mainscene.game = g
g.run()
