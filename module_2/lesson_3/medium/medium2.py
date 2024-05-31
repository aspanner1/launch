'''
P: Write a function that rotates the last count digits of a number. 
To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

E:
print(rotate_rightmost_digits(735291, 2))      # 735219
print(rotate_rightmost_digits(735291, 3))      # 735912
print(rotate_rightmost_digits(735291, 1))      # 735291
print(rotate_rightmost_digits(735291, 4))      # 732915
print(rotate_rightmost_digits(735291, 5))      # 752913
print(rotate_rightmost_digits(735291, 6))      # 352917

D: 
Input: Integer (number), Integer (number of rightmost spaces to be rotated)
Output: Integer

A: 
Turn number to be rotated into a list 
Slice the number from the 0th index to the index of the first element to be rotated
Take to-be-rotated slice
    Append first index of this slice to end 
    Delete first index 

Append start of original list with rotated second segment 
Join list with "" then turn into int

Return int

A:

Take number 
Set count = 0 
Rotate number len(number) amount 
Increment count 
Rotate number len(number) - count amount
Continue incrementing until rotating only the last 2 numbers 
Return final rotated number



'''

def max_rotation(number):
    digits_to_rotate = len(str(number))
    while digits_to_rotate >= 2:
        number = rotate_rightmost_digits(number, digits_to_rotate)
        digits_to_rotate -= 1
    
    return number

def rotate_rightmost_digits(number, rightmost_numbers_amount):
    number_as_list = list(str(number))
    start_of_rotated_section_index = 0-rightmost_numbers_amount
    first_section = number_as_list[0:start_of_rotated_section_index]
    second_section = number_as_list[start_of_rotated_section_index:]
    second_section.append(second_section[0])
    del second_section[0]
    rotated_char_list = first_section + second_section
    rotated_int = int("".join(rotated_char_list))
    return rotated_int
    


print(rotate_rightmost_digits(735291, 2))      # 735219
print(rotate_rightmost_digits(735291, 3))      # 735912
print(rotate_rightmost_digits(735291, 1))      # 735291
print(rotate_rightmost_digits(735291, 4))      # 732915
print(rotate_rightmost_digits(735291, 5))      # 752913
print(rotate_rightmost_digits(735291, 6))      # 352917

print(max_rotation(735291))         # 321579
print(max_rotation(3))              # 3
print(max_rotation(35))             # 53
print(max_rotation(105))            # 15 (the leading zero gets dropped)
print(max_rotation(8703529146))     # 7321609845