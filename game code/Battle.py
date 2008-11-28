from Character import Character

class Battle:

    #Create two characters to battle
    def __init__(self):

        self.player1 = Character('Jordan', 100, 20, 20)
        self.enemy = Character('Enemy', 80, 10, 10)


    #A method to attack the Enemy
    def attackEnemy(self):

        self.player1.attack(self.enemy)


    #A method to attack the Player
    def attackPlayer(self):

        self.enemy.attack(self.player1)

    
