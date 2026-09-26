class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.engine=self.Engine()

    class Engine:
        def __init__(self):
            self.status="Off"

        def start(self):
            self.status="Running"
            print('Engine is started')

        def stop(self):
            self.status="Off"
            print('Engine is stop')

    def drive(self):
        if self.engine.status=="Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print('Start the engine first')
car=car("Toyota","Corolla")
car.drive()
car.engine.start()
car.drive()
