class Person:
    def __init__(self, name):
        self._name = name
    
    @property 
    def name(self):
        return self._name 
    
    @name.setter 
    def name(self, other):
        if not isinstance(other, str):
            raise TypeError("Must be a string")
        if isinstance(other, str):
            if len(other) < 1:
                raise ValueError("String must have length greater than 1")
            self._name = other 
        
linda = Person('Linda')
print(linda.name)                   # Linda

linda.name = 'Lin'
print(linda.name)                   # Lin

#linda.name = ['Linda']
linda.name = ""