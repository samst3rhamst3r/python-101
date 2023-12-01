# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

str_input = input("Please input a string of characters: ").lower()

let_input = ""
while len(let_input) < 1 or len(let_input) > 1:
    let_input = input("Please input one letter to search for: ").lower()

index = str_input.index(let_input)
print(f"Letter {let_input} found at index {index}")