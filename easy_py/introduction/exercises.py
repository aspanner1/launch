def cite(author, quote):
    print(f"{author} said: {quote}")
    
def compare_by_length(string1, string2):
    string_1_length = len(string1)
    string_2_length = len(string2)
    if string_1_length > string_2_length:
        return 1
    elif string_2_length > string_1_length:
        return -1
    return 0

original_string = "Captain Ruby"
new_string = original_string[0:8] + "Python"

print(new_string)

def greet(language):
    match language:
        case 'en':
            return "Hi!"
        
def extract_language(locale):
    language=locale[:locale.index("_")]
    return language

def extract_region(locale):
    end = locale.index(".")
    start = end - 2
    locale = locale[start:end]
    return locale

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

new_numbers = []

for key in numbers.keys():
    new_numbers.append(numbers[key]//2)
    
print(new_numbers)
    