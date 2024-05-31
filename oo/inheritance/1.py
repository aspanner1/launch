class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'
    
class Bulldog(Dog):
    def sleep(self):
        return "Snoring!"

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!

