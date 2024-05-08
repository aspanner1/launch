'''
P: As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. 
If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. 
Both functions should return a value in the range 0 through 1439.

E: 

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

D: 
Input: String ("XX:"" 24 Hour Time)
Output: Integer

A: 
For before midnight:
    Split string by ":"
    Covert array to integers 
    Multiply integer at 0th index by 60
    Add integer at 1st index to this number 
    Modulo this
    Subtract the total of this addition from 1440 to get minutes before midnight

For after midnight:
    Same process as above but no subtraction

'''

def before_midnight(datetime_string):
    hours_minutes_list = datetime_string.split(":")
    integer_hours_minutes_list = [int(string_num) for string_num in hours_minutes_list ]
    total = integer_hours_minutes_list[0] * 60 + integer_hours_minutes_list[1]
    total_minutes_before_midnight = total % 1440 
    return total_minutes_before_midnight
    
print(before_midnight("00:00") == 0)     # True
print(before_midnight("12:34") == 754)   # True
print(before_midnight("24:00") == 0)     # True