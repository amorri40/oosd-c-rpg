import sys, pygame
class Splashscreen:  
    def __init__(self):
        pygame.init()
        x = 0
        background = pygame.image.load('stein.jpg')  #imports the image to display
        size = width, height = 800, 600 # sets screen dimensions
        screen = pygame.display.set_mode(size) #creates screen
        screen.blit(background, (0, 0)) # imports background into screen
        pygame.display.update()
        pygame.time.wait(3000) #screen displays for 3 seconds

splash = Splashscreen()
