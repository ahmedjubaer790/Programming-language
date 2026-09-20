class student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

s1=student("Jubaer",26)
print(s1.name)
print(s1._student__age) #this is not good practice
print(s1.__age)