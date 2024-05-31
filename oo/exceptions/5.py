
class Vehicle:
    WHEELS = 4

    @classmethod
    def wheels_info(cls):
        return f"{cls.__name__} has {cls.WHEELS} wheels."

class Bike(Vehicle):
    WHEELS = 2

class Car(Vehicle):
    pass

print(Vehicle.wheels_info())  # Output: Vehicle has 4 wheels.
print(Bike.wheels_info())     # Output: Bike has 2 wheels.
print(Car.wheels_info())      # Output: Car has 4 wheels.
