import sys, os, pygame
from pygame.locals import *
from Scene import Scene
from Battle import Battle

class BattleScreen(Scene): #Battle class for the battle screen
 def __init__(self, width=500,height=400):
    self.battle = Battle()
    pygame.init()#starts pygame
    self.width=width#sets width of window
    self.height=height#sets height of window
    self.background=pygame.image.load(os.path.join("images","battlebackground.jpg"))#loads the image ready for use
    self.screen=pygame.display.set_mode((self.width,self.height))#displays the screen
 def draw(self):
        self.update()
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.battle.enemy.getImg(),(50,220))
        self.screen.blit(self.battle.player1.getImg(),(450,250))

 def update(self):
    if self.battle.enemy.health==0:
     self.goback()
    
 def goback(self):
    self.game.currentScene=self.game.mainscene
    
 def event(self,events): 
        """
        Handle all input events here
        """
        #print "r"
        for event in events:
         if event.type == KEYDOWN:
            if event.key == K_a:#Attacks a player
                self.battle.attackEnemy()
                #print "r"
                

if __name__ == '__main__':
    pygame.init()
    running = True
 
    window = pygame.display.set_mode((300, 300)) 
    pygame.display.set_caption('RPG game coursework') 

    def input(events): 
     for event in events:         
      if event.type == QUIT:
         pygame.display.quit()
         
      else: 
         currentScene.event(events)
    
    pygame.display.flip() 
    currentScene=BattleScreen()
    #currentScene.game=Game(currentScene)
    while running: 
            input(pygame.event.get())
            pygame.display.flip() 
            currentScene.draw()