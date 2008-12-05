#A class for an Enemy

from Character import Character

class Enemy(Character):

    def __init__(self, enemyLevel):

        self.enemyL = enemyLevel
        
        self.name = 'J'
        self.health = 0
        self.attackPower = 0
        self.defense = 0

        #print str(self.getHealth())            

        self.createEnemy()

    #A method to define enemy stats
    def createEnemy(self):

        if self.getEnemyLevel() == 1:

            

            self.setName('Enemy Lv1')
            self.setHealth(20)
            self.setAttackPower(5)
            self.setDefense(5)

        elif self.getEnemyLevel() == 2:

            print 'Two'
            
            self.setName('Enemy Lv2')
            self.setHealth(30)
            self.setAttackPower(10)
            self.setDefense(10)

        elif self.getEnemyLevel() == 3:

            print 'Three'
            
            self.setName('Enemy Lv3')
            self.setHealth(40)
            self.setAttackPower(10)
            self.setDefense(10)

        elif self.getEnemyLevel() == 4:

            print 'Four'
            
            self.setName('Enemy Lv4')
            self.setHealth(50)
            self.setAttackPower(20)
            self.setDefense(20)

        elif self.getEnemyLevel() == 5:

            print 'Boss'
            
            self.setName('Boss')
            self.setHealth(150)
            self.setAttackPower(40)
            self.setDefense(60)


    def getEnemyLevel(self):

        return self.enemyL
        
        
            
