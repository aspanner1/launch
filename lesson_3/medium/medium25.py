'''
P: Write a function that computes the difference between the square of the sum of the first count positive integers 
and the sum of the squares of the first count positive integers.

E:
print(sum_square_difference(3))      # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10))     # 2640
print(sum_square_difference(1))      # 0
print(sum_square_difference(100))    # 25164150

D: 
Input: Integer
Output: Integer

A: 
Create range from 1 to submitted number + 1
Set total_sum = 0
Set sum_of_squares = 0
Iterate through range 
    Add each number to total_sum 
    Add square of each number to sum_of_squares
Square total sum

Find square of total sum - sum of squares of smaller numbers
Return this value

'''

def sum_square_difference(number):
    total_sum = 0
    sum_of_squares = 0
    for number in range(1, number + 1):
        total_sum += number 
        sum_of_squares += number**2
    
    squared_total_sum = total_sum**2
    
    return squared_total_sum - sum_of_squares

print(sum_square_difference(3))      # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10))     # 2640
print(sum_square_difference(1))      # 0
print(sum_square_difference(100))    # 25164150
