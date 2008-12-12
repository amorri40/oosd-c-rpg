#A class for an Enemy
import sys, os, pygame
from pygame.locals import *
from Character import Character

class Enemy(Character):

    def __init__(self, enemyLevel):
        print 'enemy'
        self.enemyL = enemyLevel
        
        self.name = 'J'
        self.health = 0
        self.attackPower = 0
        self.defense = 0
        self.dead = False        
        
        #print str(self.getHealth())            

        self.createEnemy()

    #A method to define enemy stats
    def createEnemy(self):

        if self.getEnemyLevel() == 1:

            
            self.setImg(pygame.image.load(os.path.join("images","scorpion.gif")))
            self.setName('Enemy Lv1')
            self.setHealth(20)
            self.setAttackPower(5)
            self.setDefense(5)
        
        #Create a slightly weak player
        elif self.getEnemyLevel() == 2:

            
            self.setImg(pygame.image.load(os.path.join("images","wolf.gif")))
            self.setName('Enemy Lv2')
            self.setHealth(30)
            self.setAttackPower(10)
            self.setDefense(10)
        
        #Create an average enemy
        elif self.getEnemyLevel() == 3:

            
            self.setImg(pygame.image.load(os.path.join("images","Straycat.gif")))
            self.setName('Enemy Lv3')
            self.setHealth(40)
            self.setAttackPower(10)
            self.setDefense(10)
        
        #Create a strong enemy
        elif self.getEnemyLevel() == 4:

           
            self.setImg(pygame.image.load(os.path.join("images","Straycat.gif")))
            self.setName('Enemy Lv4')
            self.setHealth(50)
            self.setAttackPower(20)
            self.setDefense(20)
        
        #Create a Boss level enemy
        elif self.getEnemyLevel() == 5:

            self.setImg(pygame.image.load(os.path.join("images","boss.gif")))
            self.setName('Boss')
            self.setHealth(150)
            self.setAttackPower(40)
            self.setDefense(60)


    def getEnemyLevel(self):

        return self.enemyL
        
        
            
