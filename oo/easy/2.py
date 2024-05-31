class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height
    
class Square(Rectangle):
    def __init__(self, length):
        self._length = length
        self._area = length ** 2
    
    @property
    def length(self):
        return self._length
    
    @property
    def area(self):
        return self._area
        
    
    
    
square = Square(5)
print(square.area)
print(square.area == 25)      # True