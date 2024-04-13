numbers = [1, 2, 3, 4, 5]   

new_numbers = numbers[::-1]
new_numbers = list(reversed(new_numbers))

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)

number = 42

print(number in range(10, 101))

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

result = all(isinstance(var, list) for var in [numbers, table])
print(result)

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

count = 0

print(statement1.count('t'))

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print('Spot' in ages.keys())