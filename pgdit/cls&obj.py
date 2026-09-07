#Creating class
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"{self.name} is the dog name and {self.age} is the age")
    def sit(self):
        print(f"{self.name} is now sitting")

#object
my_dog=Dog("Willie",6)
my_dog.sit()

my_dog2=Dog("Hasina",9)
my_dog2.sit()
# print(my_dog)
# print(my_dog2)