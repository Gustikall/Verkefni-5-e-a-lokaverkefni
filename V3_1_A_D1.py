# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 09/11/26
# Verkefni: Farartæki
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def drive(self):
        print("Driving!")

    def display_info(self):
        print (f"{self.brand}\n{self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, fuel_type):
        super().__init__(brand,year)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(self.fuel_type)

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_capacity):
        super().__init__(brand,year)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(self.engine_capacity)

def main():
    vehicle = Vehicle("Le Bíll", 2030)
    vehicle.drive()
    vehicle.display_info()

    car = Car("Mazda 3", 2012, "Gasoline")
    car.drive()
    car.display_info()

    motorcycle = Motorcycle("Honda", 2021, "CC150")
    motorcycle.drive()
    motorcycle.display_info()

main()