class MyClass:
    instance_count = 0  # Class variable to keep track of instance count

    def __init__(self):
        type(self).instance_count += 1  # Increment the class variable for each new instance

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count  # Class method to access the class variable
    


# Creating instances of MyClass
instance1 = MyClass()
print(f"Number of instances created: {MyClass.get_instance_count()}")  # Output: 1

instance2 = MyClass()
print(f"Number of instances created: {MyClass.get_instance_count()}")  # Output: 2

instance3 = MyClass()
print(f"Number of instances created: {MyClass.get_instance_count()}")  # Output: 3

print(instance3.__class__.__name__)
print(instance3.get_instance_count())
print(instance3.instance_count)

# This demonstrates that the instance count is correctly incremented on each new instance.
