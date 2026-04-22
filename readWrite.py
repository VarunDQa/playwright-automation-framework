file = open('test.txt')
#Read all the content of the file
#read n number of characters by passing parameters
#print(file.read())

#Read one single line at a time using readLine() method.
#print(file.readline())
#file.close()


#Print line by line using readLine method

#line = file.readline()
#while line != '':            #using WHILE condition
    #print(line)
    #line = file.readline()

#values = [Pytest, Pycharm, Python, Playwright]

for line in file.readlines():           #using FOR LOOP
    print(line)

file.close()