'''
P: Given a string of words separated by spaces, write a function that swaps the first and last letters of every word. 
You may assume that every word contains at least one letter, and that the string will always contain at least one word. 
You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

E:
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

D: 
Input: String
Output: String (modified)

A: 
Get list of all words 
Iterate through list 
    Turn every word into list
    Isolate first_letter and last_letter
    Set first letter in list to last letter
    Set last letter in list to first letter
Join new list with " "
Return as string

'''

def swap(string): 
    word_list = string.split()
    modified_word_list = []
    
    for word in word_list:
        letter_list = list(word)
        letter_list[0] = word[-1]
        letter_list[-1] = word[0]
        modified_word = ''.join(letter_list)
        modified_word_list.append(modified_word)
    
    return " ".join(modified_word_list)
    

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True