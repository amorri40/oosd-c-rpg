import pygame, sys,os
class GameObject:
    def __init__(self,x,y,imagefile,rectangle):
        self.x=x
        self.y=y
        if imagefile is not "":
         self.image=pygame.image.load(imagefile)
        else:
            self.image=""
        self.rect=rectangle #rectangle used for collision
    def draw(self,surface):
        if self.image is not "":
         surface.blit(self.image, (self.x,self.y))
        
    def collision(self):
        collision=1
    def nocollision(self):
        nocollision=1
    