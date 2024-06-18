def later2(func, first_arg):
    def second_function(second_arg):
        return func(first_arg, second_arg)
    
    return second_function

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!