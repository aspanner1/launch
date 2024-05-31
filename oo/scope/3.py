class Car:
    manufacturer = "Honda"
    
    def __init__(self, manufacturer):
        self._manufacturer = manufacturer
        
    def show_manufacturer(self):
        print(self._manufacturer)
        print(self.__class__.manufacturer)
    
civic = Car("Honka Tonka")
civic.show_manufacturer()