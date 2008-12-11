import pygame, sys,os
from gameobject import GameObject
class Npc(GameObject):
    def collision(self):
        print self.message
    def setMessage(self,dialog):
        self.message=dialog