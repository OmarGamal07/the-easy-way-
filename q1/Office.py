

class Office:
    employees=[]
    employeesNum=0
    def __init__(self,name,employess):
        self.name=name
        self.employees=employess
        self.employeesNum +=1
    @classmethod
    def get_all_employees(self):
        return self.employees
    @staticmethod
    def get_employee(self,empID):
        for emp in self.employees:
            if emp.__id == empID:
                return emp
    def hire(self,employee):
        self.employees.append(employee)
    def fire(self,empID):
        for emp in self.employees:
            if emp.__id == empID:
                self.employees.remove(emp)

    def calculate_lateness(self):
        pass

    def deduct(self,empID,deduction):
        for emp in self.employees:
            if emp.__id == empID:
                emp.__salary -= deduction

    def reward(self,empID,reward):
        for emp in self.employees:
            if emp.__id == empID:
                emp.__salary += reward

    def check_latness(self,empID,move):
        for emp in self.employees:
            if emp.__id == empID:
                late = self.check_latness(9,move,emp.distanceToWork,emp.car.velocity)
                if late <0:
                    emp.__salary -=10
                else:
                    emp.__salary +=10
    @staticmethod
    def calculate_lateness(self,target,move,distance,velocity):
        return  target - move+(distance/velocity)

    @classmethod
    def emp_changeNum(self,num):
        self.employeesNum = num