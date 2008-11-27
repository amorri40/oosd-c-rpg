import pygame, sys,os
from pygame.locals import * 
from MainScene import MainScene
 
pygame.init()
running = True
 
window = pygame.display.set_mode((300, 300)) 
pygame.display.set_caption('RPG game coursework') 

pygame.display.flip() 
 
ms = MainScene()

def input(events): 
   for event in events: 
      if event.type == QUIT:
         pygame.display.quit()
         print "quit"
      else: 
         ms.event(events) 


 
while running: 
   input(pygame.event.get())
   pygame.display.flip() 
   ms.draw()
