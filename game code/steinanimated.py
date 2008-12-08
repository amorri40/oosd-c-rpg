import pygame, pygame.movie
from pygame.locals import *

def movie():
    pygame.display.init()
    movie = pygame.movie.Movie('steinmovie.mpg')
    get_size = width, height = 300, 300
    width, height = movie.get_size()
    pygame_surface = pygame.display.set_mode(get_size)
    movie.set_display(pygame_surface)
    pygame_surface.blit(pygame_surface, (0,0))
    pygame.display.update()
    movie.play()
pygame.init()
movie2 = movie()
