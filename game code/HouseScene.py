import pygame, sys,os
from player import Player
from gameobject import GameObject
from Scene import Scene
from pygame.locals import *




class HouseScene(Scene):
    """
    The Housescene class is where the player wanders about a house level
    """
    def __init__(self):
        """
        Constructor is used to initialis the housescene
        """
        global pl
        pl = Player()
        pl.x=77
        pl.y=225
        global screen,screenbackground
        screen = pygame.display.get_surface() 
        screenbackground = pygame.Surface(pygame.display.get_surface().get_size())
        screenbackground.fill((0,0,0))
        
        """
        This is to set up the background
        """
        global background,view
        
        background = pygame.Surface((300,300))
        
        background = background.convert()
        backimg = os.path.join("images","housebackground.jpg")
        backimage = pygame.image.load(backimg)
        background.blit(backimage,(0,0))
        
        """
        This sets up the game objects
        """
        self.createObjects() 
        i=0
        while i<len(self.objects):
            self.objects[i].draw(background)
            i=i+1
            
        view = pygame.Surface((1024,1024))
        
        self.viewx=0
        self.viewy=0
        self.viewvspeed=0
        self.viewhspeed=0
        self.viewxprevious=0
        self.viewyprevious=0
        self.game = 0
    
        
    def createObjects(self):
        """
        Create the housescene game objects and puts them into the objects array,
        this should be called at the start of the scene. In here are the 
        collision blocks used for the walls and the tables in the building.
        """
        
        self.objects = [GameObject(0,0,"",pygame.Rect(0,0,300,50))]
        self.objects.append(GameObject(0,0,"",pygame.Rect(0,0,26,226)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(0,236,71,53)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(105,235,58,54)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(151,151,12,76)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(27,42,77,92)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(163,152,125,4)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(275,0,11,156)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(42,176,12,8)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(122,176,12,8)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(170,112,12,8)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(170,64,12,8)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(234,64,12,8)))
        self.objects.append(GameObject(0,0,"",pygame.Rect(234,112,12,8)))
        
    
    def update(self):
        """
        The logic of the main game is performed here. This will be called 
        everytime the player moves and the screen is redrawn.
        """
        pl.move() 
        self.checkForCollisions() 
        self.moveScene()
        
    def draw(self):
        """
        This will be called for every frame that is drawn, it will draw the 
        scene and update the game.
        """
        view.blit(background, (0, 0)) 
        
        self.update()
        
        
        pl.draw(view)
        
        screenbackground.blit(view, (self.viewx, self.viewy))
        screen.blit(screenbackground,(0,0))
        
    def moveScene(self):
        """
        Move the view so that it moves with the player
        """
        
        
        if pl.x>180 and pl.x<680:
            self.viewxprevious=self.viewx
            self.viewx = self.viewx+self.viewhspeed
        if pl.y>180 and pl.y<520:
            self.viewyprevious=self.viewy
            self.viewy = self.viewy+self.viewvspeed
        
        if self.viewx>=0:
            self.viewx=0
        elif self.viewx<=-468:
            self.viewx=-468
        if self.viewy>=0:
            self.viewy=0
        if self.viewy<=-340:
            self.viewy=-340
      
    def event(self,events): 
        """
        Handle all input events here
        """
            
        for event in events:  
          if event.type == KEYDOWN:
            pl.step = pl.step+1
            if event.key == K_ESCAPE:
              sys.exit(0)
            if event.key == K_UP:
              pl.moveUp()
              self.viewvspeed=0.2
            if event.key == K_DOWN:
              pl.moveDown()
              self.viewvspeed=-0.2
            if event.key == K_RIGHT:
              pl.moveRight()
              self.viewhspeed=-0.2
            if event.key == K_LEFT:
              pl.moveLeft()
              self.viewhspeed=0.2
          if event.type == KEYUP:
           pl.vspeed=0
           pl.hspeed=0
           self.viewhspeed=0
           self.viewvspeed=0
    
    
    
    def checkForCollisions(self):
        """
        This method checks the player rectangle against all game rectangles. 
        This is called everytime the room is drawn
        """
        playerrect = pygame.Rect(pl.x,pl.y,18,24)
        mainrect=GameObject(0,0,"",pygame.Rect(72,291,103-72,294-291))
        if (playerrect.colliderect(mainrect)):
            self.game.currentScene=self.game.mainscene
            
            
            
        i=0
        while i<len(self.objects):
            playerrect = pygame.Rect(pl.x,pl.y,18,24)
            if playerrect.colliderect(self.objects[i].rect) == 1:
                self.viewx=self.viewxprevious
                self.viewy=self.viewyprevious
                pl.x=pl.xprevious
                pl.y=pl.yprevious
                             
            i=i+1
        
    """
    This is the unit test used to test this section of the game
    by itself.
    """
if __name__ == '__main__':
    pygame.init()
    
 
    window = pygame.display.set_mode((300, 300)) 
    pygame.display.set_caption('RPG game coursework') 

    def input(events): 
     for event in events:         
      if event.type == QUIT:
         pygame.display.quit()
      else: 
         currentScene.event(events)
    
    pygame.display.flip() 
    currentScene=HouseScene()
    while True: 
            input(pygame.event.get())
            pygame.display.flip() 
            currentScene.draw()