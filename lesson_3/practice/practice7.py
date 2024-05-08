'''
P: 
Create a function that takes a list of integers as an argument 
and returns the number of identical pairs of integers in that list. 
For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. 
For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. 
The first list contains two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

E: 
print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

D: 
Input: List of numbers 
Output: Number of number pairs (as integer)

A: 
Check if list len less than 2
    If so, return 0
Create empty dictionary 
Iterate through the list
    If number not in keys list, set value to 1
    If number in keys list, increment value 
Filter dictionary to a list so that list only contains keys with values greater than 2 
Return length of list
'''

def pairs(number_list):
    if len(number_list) < 2:
        return 0
    
    number_freq_dict = {}
    for number in number_list:
        number_freq_dict[number] = number_freq_dict[number] + 1 if number in number_freq_dict.keys() else 1
    
    number_pair_list = [number for number in number_freq_dict.keys() if number_freq_dict[number] >= 2]
    
    
    count = 0
    for number in number_pair_list:
        count += number_freq_dict[number] // 2
        
    print(count)
    return count

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)