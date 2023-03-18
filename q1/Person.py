from Moods import  Moods
class Person:
    mood = ("happy", "tired", "lazy")
    def __init__(self,name,money=2000):
        self.name = name,
        self.__money = money,
        self.__mood =Person.mood[0]
        self.healthRate=100


    def setMood(self,mod):
        if mod in Moods.mood:
            self.__mood = mod

    def getMood(self):
        return self.__mood;

    def setHealth(self,rate):
        if self.healthRate >0 and self.healthRate <= 100:
            self.healthRate = rate
    def getMood(self):
        return self.healthRate

    def sleep(self,hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self,meals):
        if meals == 3:
            self.healthRate = 100

        elif meals == 2:
            self.healthRate = 75
        else:
            self.healthRate = 50

    def buy(self,items):
        if items == 1:
            self.money -= (10*items)
