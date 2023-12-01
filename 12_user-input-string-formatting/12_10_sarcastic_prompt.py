# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

honest_opinion = input("Please give us your honest opinion: ")

capitalize = False
new_str = ""
for char in honest_opinion:
    if char.isalpha():
        if capitalize:
            char = char.upper()
        else:
            char = char.lower()
        
        capitalize = not capitalize
    
    new_str += char

print(new_str)