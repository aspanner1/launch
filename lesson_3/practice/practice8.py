'''
P: Create a function that takes a non-empty string as an argument. 
The string consists entirely of lowercase alphabetic characters. The function should return the length of the longest vowel substring. 
The vowels of interest are "a", "e", "i", "o", and "u".

E:
print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

D: 
Input: String
Output: Integer

A: 
Iterate through chars in string 
    If char is not vowel, skip
    If char is vowel with no vowel preceeding it, set count = 1
    If char is vowel with vowel preceeding it, increment count
Return count

'''

vowels = 'aeiou'
def longest_vowel_substring(string):
    count_list = []
    count = 0 
    for index, char in enumerate(string): 
        if char not in vowels:
            count_list.append(count)
            count = 0
            continue
        elif char in vowels:
            count += 1
            
        if index == len(string) - 1:
            count_list.append(count)
            break
    
    return max(count_list)


print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)