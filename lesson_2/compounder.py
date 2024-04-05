def compounder(loan_amount, apr, duration_years):
    monthly_interest_rate = (apr / 100) / 12
    total_months = duration_years * 12
    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-total_months)))
    return monthly_payment

def validate_integer(potential_int):
    try:
        return int(potential_int)
    except ValueError:
        return None

while True:
    user_input = input("Please enter loan amount, APR, and duration in years, separated by spaces: ")
    info_list = user_input.split()

    if len(info_list) != 3:
        print("Please enter exactly three values.")
        continue

    loan_amount = validate_integer(info_list[0])
    apr = validate_integer(info_list[1])
    duration_years = validate_integer(info_list[2])

    if loan_amount is None or apr is None or duration_years is None:
        print("Please enter valid integer values.")
    else:
        print(f"Your monthly payment is {compounder(loan_amount, apr, duration_years)}")
        break
