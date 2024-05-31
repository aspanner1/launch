class Animal:
    @classmethod
    def speak(cls, speech):
        print(cls)
        print(speech)
    
class Cat(Animal):
    @classmethod
    def meow(cls):
        super().speak("Meow!")
        
    def test(self):
        print(self)

class Dog(Animal):
    def bark(self):
        super().speak("Woof!Woof!Woof!")
        
cat = Cat()
dog = Dog()
cat.meow()
dog.bark()