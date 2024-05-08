class Car:
    
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color 
        self.speed = 0
        self.engine_on = False
        
    @property
    def model(self):
        return self.model
    
    @model.setter
    def model(self, new_model):
        if new_model not in ['Ford', 'Chevy', 'Toyota']:
            print("Please enter a valid model!")
        
        self.model = new_model
    
        
    def ignitition(self):
        self.engine_on = not self.engine_on
        
    def accelerate(self):
        self.speed += 10 
    
    def brake(self):
        self.speed = 0 
        
    
class Person:
    def __init__(self, name):
        self._name = name
    
    @property    
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not type(self).name_validator(new_name):
            raise ValueError("Please enter a valid name")
        
        self._name = new_name
    
    @classmethod
    def name_validator(cls, new_name):
        return new_name.isalpha()
    
mike = Person("MikeyJFelix")
print(mike.name)  # Output: Mikey J Felix
mike.name = "MikeyJJ"  # Works as expected
print(mike.name)  # Output: Mikey JJ
mike.name = "123132"