'''
P: Write a function that takes a string of digits and returns the appropriate number as an integer. 
The string may have a leading + or - sign; if the first character is a +, your function should return a positive number; 
if it is a -, your function should return a negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

E: 
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

D: 
Input: String(of integers)
Output: Integer

A: 
Isolate the first character if it is not an integer
Separate it from the rest of the string 

Iterate through integer starting from the end 
Increase count of 10 for each iteration starting from 0
Multiply 10 by the integer and add to total

Return total

'''

def string_to_signed_integer(string):
    sign = "+"
    if not string[0].isnumeric():
        sign = string[0]
        string = string[1:]
    
    multiplier = 0
    total = 0
    for char in reversed(string):
            total += 10**multiplier * int(char)
            multiplier += 1
    
    total = total if sign == "+" else 0 - total
    return total
        
        
    
    
        

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True