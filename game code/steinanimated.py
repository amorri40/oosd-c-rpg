import pygame, sys, pygame.movie
from pygame.locals import *

def movie():
    global screen
    pygame.display.init()
    movie = pygame.movie.Movie("steinmovie.mpg")
    width, height = movie.get_size()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    return movie
pygame.init()
movie2 = movie()
movie2.set_display(screen)
movie2.play