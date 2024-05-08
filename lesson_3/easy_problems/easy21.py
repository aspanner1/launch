# All of these examples should print True

'''
P: 
Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. 
You should use a degree symbol (˚) to represent degrees, a single quote (') to represent minutes, 
and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

E: 
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

D: 
Input: Integer
Output: String

A: 
Multiply integer by 360 

Modulo integer by 60
Assign that result to seconds 
Divider integer by 60 with // to get floor 

Modulo integer by 60
Assign that result to minutes
Divide integer by 60 with // to get floor 

Assign final value to degrees 
Concatenate degrees, minutes, and seconds with ° , ' and \" 
Return value


'''

def dms(degrees):
    angle_in_seconds = int(degrees * 3600) 
    seconds = angle_in_seconds % 60 
    angle_in_minutes = angle_in_seconds // 60 
    minutes = angle_in_minutes % 60 
    degrees = angle_in_minutes // 60 

    angles_minutes_seconds = f"{degrees}°{minutes:02}'{seconds:02}\""
    print(angles_minutes_seconds)
    return angles_minutes_seconds

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")