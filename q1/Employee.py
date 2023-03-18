from Person import Person

import re
# from Car import  Car
class Employee(Person):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    id=0
    def __init__(self,car,distanceToWork,name,money=2000):
        super(Employee,self).__init__(name,money)
        self.__id=id+1
        self.id +=1
        self.car=car
        self.__email="abc@gmail.com"
        self.__salary=1000
        self.distanceToWork=distanceToWork
    def setEmail(self,email):
        if (re.fullmatch(self.regex, email)):
            self.__email=email
            print("Valid Email")
        else:
            print("Invalid Email")

    def getEmail(self):
        return self.__email

    def setSalary(self,salary):
        if salary >= 1000:
            self.__salary = salary
        else:
            print("must be more than 1000")

    def getSalary(self):
        return self.__salary

    def work(self,hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self,distance):
        if(distance == self.distanceToWork):
            distance = 0
        self.car.run(distance,self.velocity)

    def refuel(self,gasmount):
        self.car.fuelRate += gasmount

    @staticmethod
    def send_mail(self,to, subject, msg, receiver_name):
        file1 = open("MyFile.txt", "a")
        file1.writelines("to: "+to)
        file1.writelines("from: omar@gmail.com")
        file1.writelines("subject: " + subject)
        file1.writelines("Dear: "+receiver_name)
        file1.writelines( msg)
        file1.close()