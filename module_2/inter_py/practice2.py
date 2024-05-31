lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

def sort(list):
    return sorted(list)

sorted_lists = [sort(list) for list in lst]

print(sorted_lists)

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

dict = {item[0]: item[1] for item in lst}
print(dict)

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def odd_sum_total(list):
    return sum([number for number in list if number % 2 == 1])

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

print(sorted(lst, key=odd_sum_total))

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]


def increment_values(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}

new_list = [increment_values(value) for value in lst]

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def multiples_of_three(list):
    return [number for number in list if number % 3 == 0]

print([multiples_of_three(item) for item in lst])

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def is_vegetable(object):
    return object['type'] == 'vegetable'

def is_fruit(object):
    return object['type'] == 'fruit'

def output(item):
    if(is_vegetable(item)):
        letter_list = [string.upper() for string in item['size']]
        return "".join(letter_list)
    if(is_fruit(item)):
        return [string.capitalize() for string in item['colors']]

print([output(value) for key, value in dict1.items() ])

dict_list = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

''' 
P: Write code to return list that only contains dictionaries where all values are even

E: 
Input: Dictionary 
Output: List of dictionaries

D

A: 
Create empty list
Iterate through list of dictionaries 
    Iterate through all values in dictionary 
        If find odd number, skip value 
    By default, add dictionary to list
Print new list of dictionaries
'''

def all_values_even(dict):
    is_even = True
    for _, list in dict.items():
        for number in list: 
            if(number % 2 == 1):
                is_even = False
                break
    return is_even
            
even_only_list = [] 
print([dict for dict in dict_list if (all_values_even(dict))])

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

vowels = 'aeiou'

list_of_vowels = [char 
                  for _, list in dict1.items()
                  for string in list 
                  for char in string if char in vowels]

print(list_of_vowels)