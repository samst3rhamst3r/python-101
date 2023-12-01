# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

while True:
    num_str = input("Please choose a number between 0 and 1,000,000,000: ")
    try:
        num = int(num_str)
    except ValueError:
        continue
    
    if num < 0 or num > 1000000000:
        print("Value not within valid range. Try again.")
    else:
        break

print(num)
