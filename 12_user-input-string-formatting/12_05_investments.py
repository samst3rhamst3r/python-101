# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

def get_user_input(msg, type_t):
    
    while True:
        val = input(msg)
        try:
            val = type_t(val)
            return val
        except ValueError:
            print("Not a valid value. Try again.")

inv_amt = get_user_input("Please input an investment amount: $", float)
int_rate = get_user_input("Please input an interest in %, such as 3.5 (for 3.5%): ", float)
yrs_to_invest = get_user_input("Please input the integer number of years to invest: ", int)

total = inv_amt
for yr in range(yrs_to_invest):
    total *= (1 + int_rate / 100) ** (yr + 1)
    print(f"At end of year {yr + 1}, the future value will be ${format(total, ',.2f')}")