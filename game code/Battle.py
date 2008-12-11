from random import randint
from Character import Character
from Enemy import Enemy

class Battle:

    #Create two characters to battle
    def __init__(self):

        self.player1 = Character('Jordan', 100, 20, 20)
        ra = randint(1,4)
        self.enemy = Enemy(ra)


    #A method to attack the Enemy
    def attackEnemy(self):

        self.player1.attack(self.enemy)


    #A method to attack the Player
    def attackPlayer(self):

        self.enemy.attack(self.player1)
        
    #A method to use a special attack on an Enemy
    def useSpecialAttack(self):
        
        self.player1.specialAttack(self.enemy)

    