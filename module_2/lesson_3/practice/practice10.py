'''
P: Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. 
For example, in the case of '1432', 
the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', 
for a total of 6 substrings.

If a substring occurs more than once, 
you should count each occurrence as a separate substring.

E: 
print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

D:
Input: String of numbers
Output: Integer (number of even substrings)

A:
Create empty list
Iterate through number string putting every char in list
Iterate through number string putting every 2 char in list
    Shorten number list by len(number_list) % 2 
Iterate through number string putting every 3 char in list
    Shorten number list by len(number_list) % 3 
Continue until length of number list 

Filter through all items in list checking if even using int() and % 2 
Return length of filtered list


'''

def even_substrings(string_number):
    integer_list = []
    
    for substring_length in range(1, len(string_number) + 1):
        for index in range(len(string_number) - substring_length + 1):
            substring = string_number[index: index + substring_length]
            integer_list.append(int(substring))
    
    even_substrings = [num for num in integer_list if num % 2 == 0]

    print(even_substrings) 
    return len(even_substrings)

print(even_substrings('1432') == 6)
#print(even_substrings('3145926') == 16)
#print(even_substrings('2718281') == 16)
#print(even_substrings('13579') == 0)
#print(even_substrings('143232') == 12)
