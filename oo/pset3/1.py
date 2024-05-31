class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def __init__(self, year, bed_type):
        super().__init__(year)
        self.bed_type = bed_type
        self.start_engine()
        
    def start_engine(self):
        print('Ready to go!')

class Car(Vehicle):
    pass

'''
truck1 = Truck(1994)
print(truck1.year)            # 1994

car1 = Car(2006)
print(car1.year)              # 2006

truck1 = Truck(1994)          # Ready to go!
print(truck1.year)            # 1994

'''
# Comments show expected output
truck1 = Truck(1994, 'Short')
print(truck1.year)            # 1994
print(truck1.bed_type)        # Short

car1 = Car(2006)
print(car1.year)              # 2006
print(car1.bed_type)
# AttributeError: 'Car' object has no attribute 'bed_type'