try:
    number_1 = int(input("Please enter the first number: "))
    number_2 = int(input("Please enter the second number: "))
    result = number_1 / number_2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print(result)
finally: 
    print("End of program")