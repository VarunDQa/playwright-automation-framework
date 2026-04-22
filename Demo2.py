values = [1, 2, "Python", 6.6]
#List is data type that allows multiple values and can be different data types
print (values[0])  #1
print (values[3])  #6.6

print (values[-1])  #6.6.
print (values[0:3])  # print index from 0,1,2 but not 3, it will pick -1 data.

values.insert(3, "Test")
print (values)
values.append("Pytest")
print (values)

values[2]= "PYTHON" #Updating values
del values[0]
print (values)


#Tuple & List datatype do the same thing only difference is
# Tuple data type is immutable i.e cannot change the existing behavior, List is mutable.
# List is declared with [] & Tuple is declared using ()

#val = (1,2,"Python", 4.2)  #Tuple
val = [1,2,"Python", 4.2]   #List

val[2] = "PYTHON"
print (val[2])

#DICTIONARY: This data type is a key value pair.

dict = {"a":2, 4:"abc", "d":"Pytest"}
print (dict["a"])
print (dict[4])
print (dict["d"])

#Creating Dictionary at runtime with data addition

dict = {}

dict["firstname"] = "Test"
dict["lastname"] = "QA"

dict["Gender"] = "Male"
dict["age"] = 30

print(dict)
print(dict["firstname"])

