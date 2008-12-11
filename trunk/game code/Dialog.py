import pygame, sys,os
class Dialog:
    def __init__(self):
        dialog_img = os.path.join("images","dialogue.jpg")
        self.dialog = pygame.image.load(dialog_img)
        self.visible = False
        self.fontobject = pygame.font.Font(None,20)
        self.text = self.fontobject.render("", 1, (255,255,255), (33,33,33))
    
    def draw(self,surface,x,y):
        if self.visible == True:
            surface.blit(self.dialog, (x,y))
            # Create a text using the 'Times' system font
            
            surface.blit (self.text, (5, 35))
    def setmessage(self,message):
        self.text = self.fontobject.render(message, 1, (255,255,255))