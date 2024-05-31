class Rectangle:
    def __init__(self, width, height):
        self._width = width 
        self._height = height 
        
    @property 
    def height(self):
        return self._height 
    
    @property 
    def width(self):
        return self._width 
    
    