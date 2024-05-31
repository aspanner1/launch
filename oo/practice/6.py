class BaseClass:
    @classmethod
    def greet(self):
        print(self)
        print("Hello from BaseClass")

class SecondaryClass(BaseClass):
    pass

class ExampleClass(SecondaryClass):
    def greet(self):
        super().greet()  # Calls the `greet` method from BaseClass
        print("Hello from ExampleClass")

example = ExampleClass()
example.greet()
