count = 0

for num in range(0, 10):
    if count != 0:
        print(" " * count + "The Flintstones Rock!")
        count += 1
    else:
        print("The Flintstones Rock!")
        count += 1
        
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 3:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True