reciprocals = (1/num for num in range(1, 11))
        
for reciprocal in reciprocals:
    print(reciprocal)
    
strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

capitalize = (string.capitalize() for string in strings)

print(tuple(capitalize))

def capitalize(list_of_strings):
    for string in list_of_strings:
        yield string.capitalize()
        
print(tuple(capitalize(strings)))

capitalize = (string.capitalize() for string in strings if len(string) >= 5)
print(tuple(capitalize))