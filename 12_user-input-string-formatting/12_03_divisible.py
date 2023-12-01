# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

while True:
    val = input("Please input a number from 1 - 1,000,000: ")
    try:
        val = int(val)

        if val > 1000000 or val < 1:
            print("Invalid range of input")
            continue
        
        break
    except ValueError:
        print("Invalid entry. Please use numeric characters")
        print()

if val % 3 == 0:
    print(f"Yes {val} is divisible by 3.")
else:
    print(f"Sorry, {val} is not divisible by 3.")