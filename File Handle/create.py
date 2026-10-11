# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists

with open("testDummy.txt","x") as f:
    f.write("hello thise is new test. \n")
    f.write("I am Jubaer")

with open("testDummy.txt","r") as rd:
    print(rd.read())


