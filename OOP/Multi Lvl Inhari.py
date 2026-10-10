# Person(name, age) base class এ info(self) method "Name: <name>, Age: <age>" return করবে।
# Employee(Person) এ extra parameter emp_id। super() ব্যবহার করবে। info() override করে আগের string এর সাথে ", ID: <emp_id>" যোগ করবে।
# Developer(Employee) এ extra parameter language। info() override করে শেষে ", Language: <language>" যোগ করবে।

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        return (f"Name: <{self.name}> Age: <{self.age}>")

class Employee(Person):
    def __init__(self, name, age,id):
        super().__init__(name, age)
        self.id=id

    def info(self):
            return (super().info()+ f"ID: <{self.id}>")

class Developer(Employee):
     def __init__(self, name, age, id,language):
          super().__init__(name, age, id)
          self.language=language
     def info(self):
        return super().info() + f", Language: {self.language}"

d=Developer("Jubaer",20,101,"PL/SQL")     
print(d.info())


