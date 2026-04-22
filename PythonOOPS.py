#classes are user defined blueprint or prototype
#for e.g. a calculator: methods like sum, Multiply,addition, constant
# methods. class variables, instance variables, constructor etc.
#Self keyword is mandatory for calling variable names into method
#Constructor name should be __init__
#Instance & class keyword have whole different purpose
#new keyword is not required when new obj is created

class Calculator:
    num = 100 #class variables
    #default constructor
    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b
        print("I'm called automatically when object is created")

    def getData(self):
        print("Executing a method in class")

    def Summation(self):
        return self.firstNum + self.secondNum + Calculator.num


obj = Calculator(2,3) #syntax to create object in python
obj.getData()
print(obj.Summation())  #change the object name while running program, to avoid errors in result.


obj1 = Calculator(4,5) #syntax to create object in python
obj1.getData()
print(obj1.Summation())