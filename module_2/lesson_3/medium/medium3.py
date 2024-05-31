'''
P: 
Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.

E:
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")

D: 
Input: String (sentence)
Output: String (sentence)

A:
Split sentence into list of words
Iterate through list of words 
If word is a number, replace with integer representation 
Join new list with " "
Return new string 
'''

NUM_WORDS = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}

def modify_word(word):
    if(word in NUM_WORDS):
        return NUM_WORDS[word]
    else:
        return word
        

def word_to_digit(message):
    word_list = message.split()
    modified_word_list = [modify_word(word) for word in word_list]
    return " ".join(modified_word_list)
    
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")