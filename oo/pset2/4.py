class Cat:
    
    number_of_cats = 0
    
    def __init__(self):
        Cat.number_of_cats += 1
    
    @classmethod
    def total(cls):
        print(cls.number_of_cats)
        return cls.number_of_cats
    
    
    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")
    
Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3