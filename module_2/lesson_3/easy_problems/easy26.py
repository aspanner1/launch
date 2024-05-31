'''
P: Write a function that takes a list of integers as input, multiplies all of the integers together, 
divides the result by the number of entries in the list, 
and returns the result as a string with the value rounded to three decimal places.

E:
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

D:
Input: List
Output: String

A:
Create total with value of 1
Iterate through input list 
Set total equal to total * element in input list

Divide total by length of list 

Output with format :.3f

'''

def multiplicative_average(list):
    total = 1
    for number in list:
        total *= number
    
    total = total/len(list)
    
    return(f"{total:.3f}")

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")