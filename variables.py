def greeter(name):
    print(f"Good Morning, {name}.")
    print(f"Good Afternoon, {name}.")
    print(f"Good evening, {name}.")

def age(current_age):
    year_increments = [10, 20, 30, 40]
    for increment in year_increments:
        print(f"In {increment} years, you will be {current_age + increment} years old.")
        
def create_compound_calculator(interest_rate):
    def compound_calculator(balance, years):
        return balance * (1 + interest_rate)**years
    return compound_calculator

my_bank_compounder = create_compound_calculator(0.05)

ending_balance = my_bank_compounder(balance=1000, years=5)

print(ending_balance)
