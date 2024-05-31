'''
P: 
A featured number (something unique to this exercise) is an odd number that is a multiple of 7, 
with all of its digits occurring exactly once each. 
For example, 49 is a featured number, but 98 is not (it is not odd), 
97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. 
Issue an error message if there is no next featured number.

E: 
print(featured(12))           # 21
print(featured(20))           # 21
print(featured(21))           # 35
print(featured(997))          # 1029
print(featured(1029))         # 1043
print(featured(999999))       # 1023547
print(featured(999999987))    # 1023456987
print(featured(9876543186))   # 9876543201
print(featured(9876543200))   # 9876543201
print(featured(9876543201))   # "There is no possible number that fulfills those requirements."

D: 
Input: Integer
Output: Integer

A: 
Check if integer greater than 9876543201
    If so, return ""There is no possible number that fulfills those requirements."

Create while True loop:
    Increment number 
    Check if new number modulo 7 is 0 AND if length of number as string is same as length of number as set of chars
        If so, return that number

'''

def unique_digits(number):
    return len(str(number)) == len(set(str(number)))

def featured(number): 
    if number >= 9876543201:
        return "There is no possible number that fulfills those requirements."
    
    while True:
        number += 1
        if number % 7 == 0 and unique_digits(number):
            break
    
    return number
        
print(featured(12))           # 21
print(featured(20))           # 21
print(featured(21))           # 35
print(featured(997))          # 1029
print(featured(1029))         # 1043
print(featured(999999))       # 1023547
print(featured(999999987))    # 1023456987
print(featured(9876543186))   # 9876543201
print(featured(9876543200))   # 9876543201
print(featured(9876543201))   # "There is no possible number that fulfills those requirements."