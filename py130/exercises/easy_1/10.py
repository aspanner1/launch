def generator():
    user_text = ""
    while user_text != "stop":
        user_text = input("Please enter some text")
        yield user_text
        
    print("Program has finished running")
    
for string in generator():
    print(string)