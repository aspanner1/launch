class Pet:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self._color = color
        self._info = f"My cat {self.name} is {self.age} years old and has {self.color} fur"

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
    @property 
    def color(self):
        return self._color
    
    @property
    def info(self):
        return self._info

class Cat(Pet):
    pass

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)