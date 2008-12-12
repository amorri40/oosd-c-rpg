import pygame, sys,os
from gameobject import GameObject
class Npc(GameObject):
    """
    Non player chararcter object
    """
    def collision(self):
        """
        Show dialog when collides but only on the first collision
        """
        if self.colide == 0:
            self.di.visible=True
            self.di.setmessage(self.message)
        self.colide=self.colide+1
    def nocollision(self):
        """
        Make sure not to show dialog when no collision
        """
        self.colide = 0
    def setMessage(self,m):
        """
        set the message that the npc will say
        """
        self.message=m
    def setDialog(self,dialog):
        """
        Set the dialog object that this npc will use
        """
        self.di=dialog