import pygame, sys,os
from gameobject import GameObject
class Npc(GameObject):
    def collision(self):
        if self.colide == 0:
            self.di.visible=True
            self.di.setmessage(self.message)
        self.colide=self.colide+1
    def nocollision(self):
        self.colide = 0
    def setMessage(self,m):
        self.message=m
    def setDialog(self,dialog):
        self.di=dialog