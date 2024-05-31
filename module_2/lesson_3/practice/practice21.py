'''
P: Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. 
If there are multiple pairs that are equally close, return the pair that occurs first in the list.

E: 

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

D: 
Input: List of numbers
Output: Tuple of 2 numbers

A:
Create empty tuple
Iterate through list of numbers starting at 0
    For each number, find absolute value of that number - rest of numbers
    If that number is less than current tuple, replace that value 
    Otherwise skip 
Return minimum tuple

'''

def closest_numbers(list_of_integers):
    starting_value = abs(list_of_integers[0] - list_of_integers[1])
    current_minimum = starting_value
    current_tuple = ()
    for index, test_number in enumerate(list_of_integers):
        for number in list_of_integers[index + 1:]:
            difference = abs(test_number - number)
            if difference < current_minimum: 
                current_minimum = difference
                current_tuple = (test_number, number)
    return current_tuple


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

