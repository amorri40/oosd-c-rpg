import sys, os, pygame
from pygame.locals import *
class Splashscreen: 
    def __init__(self):
        pygame.init()
        background = pygame.image.load(os.path.join("images", "stein.jpg"))  #imports the image to display
        size = width, height = 300, 300 # sets screen dimensions
        screen = pygame.display.set_mode(size) #creates screen
        pygame.display.set_caption('RPG game coursework') #gives the program a title
        screen.blit(background, (0, 0)) # imports background into screen
        pygame.display.update()
        pygame.time.wait(3000)#screen displays for 3 seconds
        screen.fill(0)
        pygame.display.update()  #displays a black screen for a second
        pygame.time.wait(1000)