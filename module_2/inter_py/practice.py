fruits = ("apple", "banana", "cherry", "date", "banana")

def banana_counter(fruit_list):
    banana_count = 0
    for fruit in fruits:
        if(fruit == "banana"):
            banana_count += 1
    
    return banana_count

fruits.count("banana")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a_b_union = a | b

print(a_b_union)

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

total_years = 0
for(name, age) in ages.items():
    total_years += age

print(total_years)

youngest = min(ages.values())
print(youngest)

statement = "The Flintstones Rock"

letter_freq_dict = {}

for char in statement:
    letter_freq_dict.setdefault(char, 0)
    letter_freq_dict[char] += 1
    
print(letter_freq_dict)
    

