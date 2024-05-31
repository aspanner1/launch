'''
P: 
Create a function that takes a list of numbers as an argument. 
For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. 
Return the resulting list.


E: 
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

D:
Input: List of numbers 
Output: List of numbers

A: 
Create empty list
Iterate through input list of numbers 
    For each number, create a list comprehension where the filter condition is numbers less than that number
    Create set out of this list then take length of set
    Add length of set to list 
    Continue 
Output the new list

'''

def calculate_amount_of_smaller_numbers(selected_number, number_list):
    smaller_than_number_set = set([number for number in number_list if number < selected_number])
    return len(smaller_than_number_set)
    
def smaller_numbers_than_current(number_list):
    return [calculate_amount_of_smaller_numbers(number, number_list) for number in number_list]
    
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

'''
P: Create a function that takes a list of integers as an argument. 
The function should return the minimum sum of 5 consecutive numbers in the list. 
If the list contains fewer than 5 elements, the function should return None.

E: 
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

D: 
Input: List of numbers 
Output: Integer 

A: 
Check if length of integer list less than 5 
    If so, return None
Find sum of sublist from index positions 0-4. Add this sum to a list. 
Find sum of sublist from index positions 1-5. Continue until reach end of array (index position len because substring does not include end)
Find minimum from list of sums 
Output minimum
'''

def minimum_sum(integer_list):
    length = len(integer_list)
    
    if(length < 5):
        return None
    
    counter = 0
    sum_list = []
    
    while(counter + 5 <= len(integer_list)):
        sum_list.append(sum(integer_list[counter:counter + 5]))
        counter += 1
    
    print(sum_list)
    return min(sum_list) 
        
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

'''
P: Create a function that takes a string argument and returns a copy of the string 
with every second character in every third word converted to uppercase. 
Other characters should remain the same.

E:
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

D:
Input: String (sentence)
Output: String (sentence)

A: 
Split every sentence into words 
Iterate through word list 
Apply modification to every third word
    Modification function:
        Split word into characters
        Every second character (index % 2 == 0) replace value with uppercased value
    Join the word and return this value 
    Assign this value to replace original word in word list 
Join new word list 
Return new sentence
'''

def modify_word(index, word):
    if (index + 1) % 3 != 0:
        return word
    else:
        letter_list = list(word)
        for index, letter in enumerate(letter_list):
            letter_list[index] = letter.upper() if ((index + 1) % 2 == 0) else letter 
        modified_word = "".join(letter_list)
        
        return modified_word
        
            
        
        
    

def to_weird_case(sentence_string):
    word_list = sentence_string.split()
    modified_sentence = " ".join([modify_word(index, word) for index, word in enumerate(word_list)])
    print(modified_sentence)
    return modified_sentence
    
    
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

'''
P: Create a function that takes a string argument and returns a dict object 
in which the keys represent the lowercase letters in the string, 
and the values represent how often the corresponding letter occurs in the string.

E:

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})


D:
Input: String
Output: Dictionary where keys are chars and values are frequency 

A:



'''

