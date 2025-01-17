class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"The {self.year} {self.make} {self.model} is starting."

    def stop(self):
        return f"The {self.year} {self.make} {self.model} is stopping."

car_model = input("Enter the car model: ")
car_make = input("Enter the car make: ")
car_year = input("Enter the car year: ")

my_car = Car(make=car_make, model=car_model, year=car_year)
print(my_car.start())




class ElectricCar(Car):
    def charge(self):
        return f"my {self.year} {self.make} {self.model} electric car is charging"


my_electric_car = ElectricCar(car_make, car_model, car_year)
print(my_electric_car.charge())