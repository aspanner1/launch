'''
P:
Write a function that takes a string, doubles every character in the string, and returns the result as a new string.

E:
print(repeater('Hello'))        # "HHeelllloo"
print(repeater('Good job!'))    # "GGoooodd  jjoobb!!"
print(repeater(''))             # ""

D: 
Input: String 
Output: String

A: 
Iterate through string 
For every char double 
Return doubled_string
'''

def repeater(string):
    doubled_char_list = [char * 2 for char in string]
    doubled_string = "".join(doubled_char_list)
    return doubled_string


print(repeater('Hello'))        # "HHeelllloo"
print(repeater('Good job!'))    # "GGoooodd  jjoobb!!"
print(repeater(''))    

print(list(reversed(["Joe", "Roberts"])))
print(list(range(1, 5, 1)))