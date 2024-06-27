""" 
P: Convert all numbers from 1-3000 to Roman Numerals 

I = 1
V = 5
X = 10
L = 50
C = 100 
D = 500
M = 1000

E:

D: 
Input: Integer
Output: String

A: 
Modulo number by 1000, then 500, then 100, then 50, then 10, then 5, then 1
Divide number by 1000, then 500, then 100, then 50, then 10, then 5, then 1. Round down.

Append appropriate symbols
Subtract quotient from original number 
Repeat
"""

class RomanNumeral:
    ROMAN_TO_INT_DICT = {"I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
    
    def __init__(self, integer):
        self.integer = integer
        
    def to_roman(self):
        roman_numerals = ""
        current_value = self.integer
        desc_roman_int_tuples = reversed(list(self.__class__.ROMAN_TO_INT_DICT.items()))
        
        for roman, number in desc_roman_int_tuples:
            number_of_numerals = current_value // number
            roman_numerals = roman_numerals + (roman * number_of_numerals) 
            current_value = current_value % number 
            
        return roman_numerals
            
        