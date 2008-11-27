import pygame, sys,os
from player import Player
from gameobject import GameObject
from pygame.locals import * 

class MainScene:
    """
    The Mainscene class is where the main game takes place.
    """
    def __init__(self):
        """
        Constructor used for initialising the main scene
        """
        global pl
        pl = Player()
        global screen,screenbackground
        screen = pygame.display.get_surface() 
        screenbackground = pygame.Surface(pygame.display.get_surface().get_size())
        screenbackground.fill((0,0,0))
        
        """
        Setup background
        """
        global background,view
        
        background = pygame.Surface((1042,1024))
        
        background = background.convert()
        backimg = os.path.join("images","background.png")
        backimage = pygame.image.load(backimg)
        #background.fill((51, 153, 0))
        background.blit(backimage,(0,0))
        
        """
        Setup game objects
        """
        #Now create all the game objects
        self.createObjects() 
        #draw the objects one by one on to the background image
        i=0
        while i<len(self.objects):
            self.objects[i].draw(background)
            i=i+1
        #create a new view which will be the main play area
        view = pygame.Surface((1024,1024))
        
        self.viewx=0
        self.viewy=0
        self.viewvspeed=0
        self.viewhspeed=0
        self.viewxprevious=0
        self.viewyprevious=0
    
        
    def createObjects(self):
        """
        Create the main game objects and put the into the objects array,
        this should be called at the start of the scene.
        """
        self.objects = [GameObject(20,20,os.path.join("images","player.png"),pygame.Rect(20,20,18,24))]
        self.objects.append(GameObject(200,200,os.path.join("images","player.png"),pygame.Rect(200,200,18,24)))
    
    def draw(self):
        """
        This will be called for every frame that is drawn, it will
        draw the scene and update the game.
        """
        view.blit(background, (0, 0)) #draw the background image onto the view
        
        pl.move() #move the player to the new position
        self.checkForCollisions() #check if the player collides with any game object
        
        pl.draw(view)#draw the player
        self.moveScene()#move the scene when the player moves
        screenbackground.blit(view, (self.viewx, self.viewy))#draw the view onto screenbackground
        screen.blit(screenbackground,(0,0))#draw the main game to the screen
        
    def moveScene(self):
        """
        Move the view so that it moves with the player
        """
        if self.viewx<700:
          self.viewxprevious=self.viewx
          self.viewx = self.viewx+self.viewhspeed
        else:
            pl.x=0
            self.viewx=self.viewxprevious
        if self.viewy<700:
            self.viewyprevious=self.viewy
            self.viewy = self.viewy+self.viewvspeed
        
    
      
    def event(self,events): 
        """
        Handle all input events here
        """
            
        for event in events:  
          if event.type == KEYDOWN:
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
        This method checks the player rectangle against all game rectangles
        This is called everytime the room is drawn
        """
        i=0
        while i<len(self.objects):
            playerrect = pygame.Rect(pl.x,pl.y,18,24)
            if playerrect.colliderect(self.objects[i].rect) == 1:
                self.viewx=self.viewxprevious
                self.viewy=self.viewyprevious
                pl.x=pl.xprevious
                pl.y=pl.yprevious
              
            i=i+1
        
