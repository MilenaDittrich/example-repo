import math
# purpose:user to calc. int on investment or repayments on home loan
# user either chooses bond or investment should not be case sensetive

# get user to choose either bond or investment should not be case sensitive
# if neither error message should show
# lower to make everything lowercase so that it is not case sensitive
bond_or_investment = input("Do you want to check youre bond or investment?: ").lower()
print(bond_or_investment)

# if-elif-else for results for bond_or_investment
if bond_or_investment == "investment":
    # determine user inputs
    present_value = float(input("Do you know what the present value of your investment is?: "))
    interest_rate = float(input("At what interest rate will your deposit be?: "))
    years = float(input("How many years will your deposit be maturing for?: "))
    print(f"You are depositing {present_value} at {interest_rate}% for {years} years.")


  # detrmine if they are using simple or compound interest
    interest = input("Are you using simple or compound: ").lower()

    if interest == "simple":
        # Calculate and print out maturity
        future_value = present_value * (1 + interest_rate*years)
        print(f"You will recieve R{future_value} at the investments maturity.")

    elif interest == "compound":
        # Calculate and print out maturity
        interest_rate_div_hundered = interest_rate % 100
        future_value= present_value * math.pow((1+interest_rate_div_hundered),years)
        print(f"You will recieve R{future_value} at the investments maturity.")
    else:
        print("You have not entered either simple or compound interest correctly.")
        print("Please try again.")

elif bond_or_investment == "bond":
    # use f-string to determine formula inputs
    present_value = float(input("What is the present value of your house?: "))
    interest_rate = float(input("What is your interest rate?: "))
    months = float(input("How many months will your bond be maturing over?: "))

    print(f"Your house is currently worth {present_value}.")
    print(f"Your bond matures at {interest_rate}% per annum.")
    print(f"Your planning to take {months} to repay your bond.")

    # calculate and print out bond repayment
    # making interest a percentage
    interest_pre = int(interest_rate) % 100
    interest= interest_pre % 12 #dividing by months
    repayment = (interest * present_value)/(1 - (1 + interest)**(-months))

    print(f"You will pay R{repayment} per month.")

else:
    # Limiting line length by spliting sting
    print("Unfortunatley you have not enterd a sufficient answser.")
    print("Please type either investment or bond next time.")
