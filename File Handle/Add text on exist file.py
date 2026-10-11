f=open("D:\\Python Prc & Environment\\python\\File Handle\\dummy.txt","a")
f.write("\nHello i am Jubaer")
f.close

f=open("D:\\Python Prc & Environment\\python\\File Handle\\dummy.txt","r")
print(f.read())
f.close()

# "r" for read, and "t" for text are the default values, you do not need to specify them.
f = open("demofile.txt", "rt")