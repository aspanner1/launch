class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")
        
class Cat(Animal):
    def __init__(self, name, age, status):
        super().__init__(name, age, 4, "cat", status)
    
    def introduce(self):
        return f"{super().introduce() + " " + "Meow meow!"}" 
        
        
        
        

cat = Cat("Pepe", 4, "happy")
expected = ("Hello, my name is Pepe and I am 4 years old "
            "and happy. Meow meow!")
print(cat.introduce())
print(cat.introduce() == expected)      # True