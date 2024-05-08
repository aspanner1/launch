class Car:
    def __init__(self, id, year, color):
        self.id = id 
        self.year = year
        self.color = color 
    
    def __str__(self):
        return f"{self.id} {self.year} {self.color}"
    
    
vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        return self.x * other.x + other.y * self.y

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 * v2) # 17
print(v1 + v2)      # Vector(18, 8)