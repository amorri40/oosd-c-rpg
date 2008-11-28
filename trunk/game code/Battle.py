from Character import Character

class Battle:

    #Create two characters to battle
    def __init__(self):

        player1 = Character(100, 20, 20)
        enemy = Character(80, 10, 10)


    #A method to attack the Enemy
    def attackEnemy(self):

        player1.attack(self.enemy)


    #A method to attack the Player
    def attackPlayer(self):

        enemy.attack(self.player1)

    
