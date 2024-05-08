'''
P:
Write a function that counts the number of occurrences of each element in a given list. 
Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

E: 
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

D: 
Input: List of strings
Output: String => integer 

A: 
Create empty dictionary 
Iterate through list 
If string in dictionary
    Increment value by one 
If string not in dictionary 
    Set value to one 

Iterate through set in element => count format 
'''
def count_occurrences(vehicle_list):
    vehicle_count = {}
    for vehicle in vehicle_list:
        vehicle_count[vehicle] = vehicle_count[vehicle] + 1 if vehicle in vehicle_count.keys() else 1
    
    for vehicle, count in vehicle_count.items():
        print(f"{vehicle} => {count}")
        
        
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)