pi = 3.141592
str_pi = str(pi)

'''
for number in range(3, 17, 4):
    print(number)
'''

country_origins_dict = {
    'Alice':'USA',
    'Francois':'Canada',
    'Inti': 'Peru',
    'Monika':'Germany',
    'Sanyu':'Uganda',
    'Yoshitaka':'Japan',
}

#print(country_origins_dict['Alice'])

sixth_digit = range(0, 25, 3)[6]

print(sixth_digit)

name = "Launch School"
c_index = name.find('c')

print(name[c_index: c_index + 6])

values = (1, 2, 3, 4, 5)

print(list(reversed(values))[1:4])

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

cocoa_activities = cats['Pete']['Cocoa']['enjoys']

for activity in cocoa_activities:
    print(activity)

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

all_number_sets = [numbers1, numbers2, numbers3, numbers4, numbers5]


for number_set in all_number_sets:
    print(3 in number_set)
    
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

zipped = zip(my_str, my_list, my_tuple, my_range)
print(list(zipped))