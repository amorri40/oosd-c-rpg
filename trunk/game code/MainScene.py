import pygame, sys,os
from player import Player
from gameobject import GameObject
from Scene import Scene
from pygame.locals import * 

class MainScene(Scene):
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
        backimg = os.path.join("images","background2.png")
        backimage = pygame.image.load(backimg)
        backimg_above = os.path.join("images","background2_above.png")
        self.backimage_above = pygame.image.load(backimg_above)
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
        self.game = 0
    
        
    def createObjects(self):
        """
        Create the main game objects and put the into the objects array,
        this should be called at the start of the scene.
        """
        
        self.objects = [GameObject(20,20,os.path.join("images","player.png"),pygame.Rect(20,20,18,24))]
        #self.objects.append(GameObject(200,200,os.path.join("images","player.png"),pygame.Rect(200,200,18,24)))
        #self.objects.append(GameObject(0,0,"",pygame.Rect(16,32,736-16,608-32)))#collision for boundary
        self.objects.append(GameObject(200,200,"",pygame.Rect(48,96,190-48,176-96)))#collision for a building
        self.objects.append(GameObject(200,200,"",pygame.Rect(240,96,432-240,176-96)))#collision for a building
        self.objects.append(GameObject(200,200,"",pygame.Rect(512,96,720-512,192-96)))#collision for a building
        self.objects.append(GameObject(48,224,"",pygame.Rect(48,224,240-48,304-208)))#collision for a building
        self.objects.append(GameObject(288,224,"",pygame.Rect(288,224,432-288,304-224)))#collision for a building
        self.objects.append(GameObject(192,352,"",pygame.Rect(192,352,432-192,432-352)))#collision for a building (eating place)
        self.objects.append(GameObject(48,480,"",pygame.Rect(48,480,240-48,560-480)))#collision for a building (potion)
        self.objects.append(GameObject(288,480,"",pygame.Rect(288,480,432-288,560-480)))#collision for a building(house)
        self.objects.append(GameObject(512,415,"",pygame.Rect(512,415,720-512,575-415)))#collision for a building (church)
        
        self.objects.append(GameObject(0,0,"",pygame.Rect(0,0,14,640)))#collision for left boundary
        self.objects.append(GameObject(751,0,"",pygame.Rect(751,0,14,640)))#collision for right boundary
        self.objects.append(GameObject(0,608,"",pygame.Rect(0,608,768,30)))#collision for bottom boundary
        self.objects.append(GameObject(0,0,"",pygame.Rect(0,0,447,15)))#collision for top left boundary
        self.objects.append(GameObject(496,0,"",pygame.Rect(496,0,300,15)))#collision for top right boundary

        
        self.objects.append(GameObject(0,50,"",pygame.Rect(0,50,447,19)))#collision for water left
        self.objects.append(GameObject(496,48,"",pygame.Rect(496,48,300,19)))#collision for water right

    
    def update(self):
        """
        This method will be called everytime the game is drawn to update the player and other game 
        objects to new positions. Main game logic is performed here.
        """
        pl.move() #move the player to the new position
        self.checkForCollisions() #check if the player collides with any game object
        self.moveScene()#move the scene when the player moves
        pl.checkbattle()#check if random battle has occured
        
    def draw(self):
        """
        This will be called for every frame that is drawn, it will
        draw the scene and update the game.
        """
        view.blit(background, (0, 0)) #draw the background image onto the view
        
        self.update()#update the scene
        
        
        pl.draw(view)#draw the player
        
        screenbackground.blit(view, (self.viewx, self.viewy))#draw the view onto screenbackground
        screenbackground.blit(self.backimage_above,(self.viewx, self.viewy))
        screen.blit(screenbackground,(0,0))#draw the main game to the screen
        
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
        
