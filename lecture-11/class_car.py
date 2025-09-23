class Car:
    wheels = 4 

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is now running."
    
    def stop_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is now off."
    
my_car = Car("Toyota", "Corolla", 2020)

print(my_car.make)
print(my_car.model)
print(my_car.year)

print(my_car.start_engine())
print(my_car.stop_engine())
