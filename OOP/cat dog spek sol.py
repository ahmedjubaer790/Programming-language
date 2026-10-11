# ---------- Step 1: Base Class ----------
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Name: {self.name}, Age: {self.age}, Sound: Wow")


# ---------- Step 2 ও 3: Child Classes ----------
class Dog(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)   # parent এর __init__ কল
        self.type = type              # নতুন property

    def speak(self):
        print(f"Name: {self.name}, Age: {self.age}, Type: {self.type}, Sound: Woof")


class Cat(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

    def speak(self):
        print(f"Name: {self.name}, Age: {self.age}, Type: {self.type}, Sound: Meow")


# ---------- Step 4: Objects তৈরি ও speak() কল ----------
dog = Dog("Max", 20, "German Shephard")
cat = Cat("Kitty", 10, "Persian")

dog.speak()
cat.speak()