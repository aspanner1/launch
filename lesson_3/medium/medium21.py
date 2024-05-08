'''
P: 
Write a function that takes a string and returns an object containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
You may assume that the string will always contain at least one character.

E: 

print(letter_percentages('abCdef 123'))
# { 'lowercase': "50.00", 'uppercase': "10.00", 'neither': "40.00" }

print(letter_percentages('AbCd +Ef'))
# { 'lowercase': "37.50", 'uppercase': "37.50", 'neither': "25.00" }

print(letter_percentages('123'))
# { 'lowercase': "0.00", 'uppercase': "0.00", 'neither': "100.00" }

D: 
Input: String 
Output: Dictionary of lowercase, uppercase, and neither percentages

A:
Iterate through every character in string 
    If is_lowercase, increase count lowercase
    If is_uppercase, increase count uppercase
    If is not a char, increase count non_char

Return total counts divided by length of string in dictionary list formatted .2f 
'''

def letter_percentages(string):
    lowercase_count = 0
    uppercase_count = 0 
    nonchar_count = 0
    total_length = len(string)
    
    lowercase_percentage = (len(([char for char in string if char.islower()]))/total_length) * 100
    uppercase_percentage = (len([char for char in string if char.isupper()])/total_length) * 100
    nonchar_percentage = (len([char for char in string if not char.isalpha()])/total_length) * 100
    
    percentage_dictionary = {'lowercase': f"{lowercase_percentage:.2f}", 'uppercase': f"{uppercase_percentage:.2f}", nonchar_percentage: f"{nonchar_percentage:.2f}"}
    return percentage_dictionary
    
    
print(letter_percentages('abCdef 123'))
# { 'lowercase': "50.00", 'uppercase': "10.00", 'neither': "40.00" }

print(letter_percentages('AbCd +Ef'))
# { 'lowercase': "37.50", 'uppercase': "37.50", 'neither': "25.00" }

print(letter_percentages('123'))
# { 'lowercase': "0.00", 'uppercase': "0.00", 'neither': "100.00" }
    