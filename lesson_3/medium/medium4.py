'''
P: The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1. 
The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. 

E: Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to the function:

D: 
Input: Integer
Output: Integer

A: 
Create list of [1, 1]
If submitted number is 1 or 2, return values at index 0 and 1
Create for loop that will iterate from 1 to submitted number - 2 times
    For each iteration, append value created from adding two previous numbers in list 
Return value at index position [-1]

'''

def fibonacci(integer):
    if(integer == 1 or integer == 2):
        return 1
    
    fibonacci_list = [1, 1]
    for i in range(1, integer - 1):
        fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i - 1])
    
    print(fibonacci_list[-1])
    return fibonacci_list[-1]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
#print(fibonacci(50) == 12586269025)       # True
#print(fibonacci(75) == 2111485077978050)  # True