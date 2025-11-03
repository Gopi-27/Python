class Car:
    def __init__(self, make, model, year):  
        self.make = make        
        self.model = model      
        self.year = year        
        self.is_running = False 

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model} is now starting.")
        else:
            print(f"{self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.year} {self.make} {self.model} has been stopped.")
        else:
            print(f"{self.year} {self.make} {self.model} is already stopped.")


my_car = Car("Toyota", "Camry", 2022)
my_car.start()
my_car.stop()
