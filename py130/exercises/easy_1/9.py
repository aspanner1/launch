def generator_function():
    count = 0
    while count <=5:
        yield count
        count += 1
        
print(list(generator_function()))
        