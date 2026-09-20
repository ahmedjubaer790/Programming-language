#Parent class is a common class that is used for every child class.
class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def start(self):
        print(f"{self.brand} {self.model} is starting")

#child class
class bike(vehicle):
    def __init__(self,brand,model,tyre):
        super().__init__(brand,model)

        #bike attributes 
        self.tyre=tyre

        #we can add child own method
    def open_tr(self):
        print('Bike tyres are opening')

b1=bike("Yamaha","R15",2)
b1.start()
b1.open_tr()

#2nd child
class car(vehicle):
    def __init__(self,brand,model,tyre):
        super().__init__(brand,model)
        self.tyre=tyre
    def open_tr(self):
        print('Car tyres are runnig now') 

c1=car("Toyota","Corolla",4)
c1.start()
c1.open_tr()