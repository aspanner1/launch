class Vehicle: 
    vehicle_number = 0 
    
    @classmethod
    def vehicles(cls):
        return cls.vehicle_number
    
    def __init__(self):
        Vehicle.vehicle_number += 1 
        
    

class Car(Vehicle):
    pass
        
class Truck(Vehicle):
    pass

class Boat(Vehicle):
    pass

print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8