# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

str_1 = input("Please input string 1: ")
str_2 = input("Please input string 2: ")
str_3 = input("Please input string 3: ")

max_str = ""
for s in [str_1, str_2, str_3]:
    if len(s) > len(max_str):
        max_str = s

print(f"{len(max_str)}, {max_str}")