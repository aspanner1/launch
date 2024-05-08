'''
P:
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, 
and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments 
and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

E: 
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

D: 
Input: Integer, Integer, Integer
Output: String (equilateral, isosceles, scalene)

A:
Put all numbers into list
Turn list into set 
Validity checker:
    Create sorted list 
    If index 0 + index 1 are less than index 2, return "invalid"
    If 0 in list, return "invalid"

If length of set = 3, its scalene
If length of set = 2, isosceles
If length of set = 1, equilateral



'''

def triangle(side1, side2, side3):
    length_list = sorted([side1, side2, side3])
    if(length_list[0] + length_list[1] < length_list[2]):
        return "invalid"
    elif(0 in length_list):
        return "invalid"
    
    length_set = set(length_list)
    
    match len(length_set):
        case 1:
            return "equilateral"
        case 2:
            return "isosceles"
        case 3:
            return "scalene"
    

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True