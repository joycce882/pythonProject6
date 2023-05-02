filename = 'test.txt'
with open(filename, 'w') as file_object:
    file_object.write("Hello World\n")
    file_object.write("I love Programming\n")
with open(filename, 'a') as file_object2:
    file_object2.write("Test file")
