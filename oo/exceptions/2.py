class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)

num = float(input('Enter a number: '))
if num < 0:
    raise NegativeNumberError("This is a negative number!")
print(f'You entered {num}')

