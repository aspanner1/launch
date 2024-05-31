'''
P: Create a function that takes a string as an argument and returns True if the string is a pangram,
False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once. 
For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. 
Note that case is irrelevant.

E: 
print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

D:
Input: String 
Output: Boolean

A: 
Create a dictionary of every letter with a value of false 
Iterate through the string
    If is letter:
        Lowercase the letter 
        dictionary[letter] = True
    Filter through all values in dictionary.
    
'''

import string
import copy

LETTER_DICT = {letter: False for letter in string.ascii_lowercase}

def is_pangram(string): 
    this_letter_dict = copy.copy(LETTER_DICT)
    for char in string:
        if char.isalpha():
            this_letter_dict[char.lower()] = True
        else:
            continue
    
    return all(this_letter_dict.values())
    
print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)