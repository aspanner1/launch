class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return f'bark! bark! {self.name} bark! bark!'

teddy = Dog('Teddy', 'Golden Retriever')
print(teddy.speak())         # bark! bark! Teddy bark! bark!
print(teddy.get_name())      # Teddy
print(teddy.get_breed())     # Golden Retriever