#Inheritance: acquiring properties of Parent class in child class.
#Without redefining properties or methods again, you can simply inherit all the properties from your parent to child class.
from PythonOOPS import Calculator

class Inherit(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2,10)

    def getFullData(self):
        return self.num2 + self.num + self.Summation()

obj = Inherit()
print(obj.getFullData())