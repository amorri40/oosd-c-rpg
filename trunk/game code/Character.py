

class Character:

    #Set up a character with a certain attributes
    def __init__(self, health, attackPower, defense):

        #self.name = name
        self.health = health
        self.attackPower = attackPower
        self.defense = defense


    #Set the Character's health to a specified integer
    def setHealth(self, h):

        self.health = h


    #Get the Character's health
    def getHealth(self):

        return self.health


    #Set the Character's attack power
    def setAttackPower(self, a):

        self.attackPower = a


    #Get the Character's attack power
    def getAttackPower(self):

        return self.attackPower


    #Set the Character's defense
    def setDefense(self, d):

        self.defense = d


    #Get the character's defense
    def getDefense(self):

        return self.defense


    #Get the Character's name
    def getName(self):

        return self.name


    #A method to attack another Character
    def attack(self, pl):

        temp = pl.getHealth() - self.attackPower
        pl.setHealth(temp)

        print "Hello!"


       




        
