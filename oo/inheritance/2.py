class Animal:
    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Animal):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'
    
class Cat(Animal):
    def speak(self):
        return 'meow!'