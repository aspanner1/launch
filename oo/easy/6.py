class WalkMixIn:
    def walk(self):
        return f"{self.name} {self.gait()} forward"

class Person(WalkMixIn):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(WalkMixIn):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixIn):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    
class Noble(WalkMixIn):
    def __init__(self, name, title):
        self._name = name
        self._title = title
    
    @property 
    def name(self):
        return self._name 
    
    def gait(self):
        return "struts"
    
    @property
    def title(self):
        return self._title
    
    def walk(self):
        return f"{self.title} {self.name} {self.gait()} forward"
    
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"