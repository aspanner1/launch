#number_list = [] 

#for number in range(1, 7):
    #number = int(input("Please enter a number: "))
    #number_list.append(number)
    
#six_in_first_five = number_list[5] in number_list[0:5]

#print(six_in_first_five)

def running_total(int_list):
    list = []
    running_total = 0
    for number in int_list:
        running_total += number
        list.append(running_total)
        
    return(list)
        
    

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

from collections import defaultdict

def word_sizes(string):
    length_dict = defaultdict(int)  # Initializes missing keys with an int, which defaults to 0
    for word in string.split():
        length_dict[len(word)] += 1
    return length_dict

    

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})