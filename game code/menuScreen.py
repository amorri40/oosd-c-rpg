import sys, os, pygame
from pygame.locals import *
from Scene import Scene

class menuScreen(Scene): #Menu class for the menu screen
 def __init__(self, width=300,height=300):
    pygame.init()#starts pygame
    self.width=width#sets width of window
    self.height=height#sets height of window
    self.background=pygame.image.load(os.path.join("images","menuScreen.jpg"))#loads the image ready for use
    self.screen=pygame.display.set_mode((self.width,self.height))#displays the screen
 def draw(self):
        self.screen.blit(self.background,(0,0))
 def update(self):
    u=1
    
 def event(self,events): 
        """
        Handle all input events here
        """
        for event in events:
            if event.key == K_RETURN:#starts the game
                self.game.gotoMain()
            if event.key == K_ESCAPE:#quits the game
                sys.exit(0)



