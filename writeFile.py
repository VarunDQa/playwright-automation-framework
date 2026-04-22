#read the file & store all lines in the list
# reverse the list
#write the list back to file

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)




