greeting = "Hello Python"
a=4
if a > 2: #greeting == "Hello Python":   #Rules: add : after condition and follow coding indentations

    print("condition is matched")
else:
    print("condition does not match")

print("IF ELSE condition is completed")


#FOR loop
obj = [2,3,5,7,9]
for i in obj:
    print(i*2)
#Sum of first 5 natural numbers: 1+2+3+4+5=15
#range(i,j) -> i to j-1
summation = 0
for j in range(1,6):      #for(i=0;i<5;i++) in Java
    summation += j
    print(j)
print(summation)


# Programming loops using For Loop
print("*****************************************************************")
for k in range(1,10,2):
    print(k)

print("***********************SKIPPING 1st INDEX***************************")
for j in range(10):
    print(j)