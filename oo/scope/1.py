class Dog:
    def __init__(self, breed):
        self._breed = breed 
    
    def get_breed(self):
        return self._breed 
    
class Cat:
    def get_name(self):
        return self._name 
    
golden_retriever = Dog("Golden Retriever")
poodle = Dog("Poodle")


