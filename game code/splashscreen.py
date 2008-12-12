import sys, os, pygame
from pygame.locals import *
class Splashscreen: 
    def __init__(self):
        pygame.init()
        background = pygame.image.load(os.path.join("images", "stein1.jpg"))  #imports the image to display
        size = width, height = 300, 300 # sets screen dimensions
        screen = pygame.display.set_mode(size) #creates screen
        pygame.display.set_caption('RPG game coursework') #gives the program a title
        screen.blit(background, (0, 0)) # imports background into screen
        pygame.display.update()
        pygame.time.wait(1000)#screen displays for 3 seconds
        background2 = pygame.image.load(os.path.join("images", "stein2.jpg"))
        screen.blit(background2, (0,0))
        pygame.display.update()
        pygame.time.wait(1000)
        background3 = pygame.image.load(os.path.join("images", "stein3.jpg"))
        screen.blit(background3, (0,0))
        pygame.display.update()
        pygame.time.wait(1000)
splash = Splashscreen()
running=True
print "please hold down the space bar to load the menu"
while running:
 for event in pygame.event.get():  
          if event.type == KEYDOWN:
            if event.key == K_SPACE: #if wanting program to terminate hold 
             running= False           #enter down
            
 splash = Splashscreen()        