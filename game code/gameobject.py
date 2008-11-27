import pygame, sys,os
class GameObject:
    def __init__(self,x,y,imagefile,rectangle):
        self.x=x
        self.y=y
        self.image=pygame.image.load(imagefile)
        self.rect=rectangle #rectangle used for collision
    def draw(self,surface):
        surface.blit(self.image, (self.x,self.y))