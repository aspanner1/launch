def later(func, argument):
    def default():
        return func(argument)
    
    return default

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!