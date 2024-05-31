class Cat:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name == other.name 
    
cat1 = Cat("Mochi")
cat2 = Cat("Kitty")
cat3 = Cat("Mochi")

print(cat1 == cat2)
print(cat1 == cat3)