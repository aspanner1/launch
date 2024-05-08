"""
Problem: 
Given a list of strings, return a new list where the strings are sorted based on the highest number of adjacent consonants a string contains. 
If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. 
Consonants are considered adjacent if they are next to each other in the same word or if there is a space 
between two consonants in adjacent words.

Input: List of strings
Output: List where strings sorted based on number of adjacent consonants 

Explicit: 
If two strings contain same # adjacent consonants, maintain original order
Adjacent consonants can be either next to each other or space in between

Q:
What order to sort?

Examples and Test Cases: 
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

Notes:
Not all strings in list will have adjacent consonants
Order from most adjacent consonants to least 

Data Structure:
Integer to count adjacent consonants
Dictionary with key being string and value being # of adjacent consonants
Output list

Algorithm:
Create CONSTANT list of consonants
Create CONSTANT list of vowels
Create function to determine if two character arguments are adjacent consonants
Iterate through list of whitespace stripped strings
    Iterate through string in letter-pairs
        Increment count if letter-pairs are consonants
    Create string as key and # consonants as value in dictionary

Get all dictionary items and sort them by value in descending order
Return sorted strings as a list
        
"""

def is_vowel(char):
    vowels = "aeiou"
    return char in vowels

def is_consonant(char):
    return char.isalpha() and not is_vowel(char)

def is_consonant_pair(two_char_list):
    return is_consonant(two_char_list[0]) & is_consonant(two_char_list[1])

def eliminate_white_space(string):
    return ''.join(string.split())
    

def sort_by_consonant_count(string_list):
    string_pair_number_dict = {}
    for string in string_list:
        adjacent_consonant_pairs = 0
        string_without_whitespace = eliminate_white_space(string)
        for index, _ in enumerate(string_without_whitespace[:-1:]):
            potential_pair = list(string_without_whitespace[index:index + 2])
            print(f"Potential pair: {potential_pair}")
            if(is_consonant_pair(potential_pair)):
                adjacent_consonant_pairs += 1
        string_pair_number_dict[string] = adjacent_consonant_pairs
        print(string_pair_number_dict)
        
    sorted_tuples_with_values = sorted(string_pair_number_dict.items(), key = lambda x: x[1], reverse=True)
    sorted_strings = dict(sorted_tuples_with_values).keys() 
    
    return sorted_strings
            
            
        

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']