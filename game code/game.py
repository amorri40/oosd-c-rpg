import pygame, sys,os
from pygame.locals import * 
from MainScene import MainScene
from splashscreen import Splashscreen
from HouseScene import HouseScene


from BattleScene     import BattleScreen
from menuScreen import menuScreen

 







class Game:
    """
    The game class used fro running the game
    """
    def __init__(self,scene=None):
        self.mainscene=MainScene()
        if scene==None:
         
         self.currentScene = menuScreen()#self.mainscene
         
        else:
            self.currentScene=scene
        self.currentScene.game=self    
        
        
        #splash = Splashscreen()
    def run(self):
        """
        The run method to run the whole game the main game loop
        """
        while running: 
            self.input(pygame.event.get())
            pygame.display.flip() 
            self.currentScene.draw()
            
    def gotoHouse(self):
        self.currentScene=HouseScene()
        self.currentScene.game=self.mainscene.game
    def gotoMain(self):
        self.currentScene=self.mainscene#MainScene()
        #self.currentScene.game=self    
        
    def input(self,events): 
     for event in events:         
      if event.type == QUIT:
         pygame.display.quit()
         print "quit"
      else: 
         self.currentScene.event(events) 

if __name__ == '__main__':
 pygame.init()
 running = True
 
 window = pygame.display.set_mode((300, 300)) 
 pygame.display.set_caption('RPG game coursework') 

 pygame.display.flip() 
 
 ms = menuScreen()
 g = Game(ms)
 g.mainscene.game = g
 g.run()
