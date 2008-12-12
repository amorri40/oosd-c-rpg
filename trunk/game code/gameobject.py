import pygame, sys,os
class GameObject:
    """
    Game object class used for collisions
    """
    def __init__(self,x,y,imagefile,rectangle):
        self.x=x
        self.y=y
        if imagefile is not "":
         self.image=pygame.image.load(imagefile)
        else:
            self.image=""
        self.rect=rectangle #rectangle used for collision
    def draw(self,surface):
        """
        Draw the image if it is set
        """
        if self.image is not "":
         surface.blit(self.image, (self.x,self.y))
        
    def collision(self):
        """
        Only used for npcs
        """
        collision=1
    def nocollision(self):
        """
        Only used for npcs
        """
        nocollision=1
    