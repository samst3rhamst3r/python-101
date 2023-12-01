# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"

valid = False
valid_prev_char = None
for char in filename:
    if (char == ".") or (valid_prev_char == "." and char == "p") or (valid_prev_char == "p" and char == "d"):
        valid_prev_char = char
    elif (valid_prev_char == "d" and char == "f"):
        valid_prev_char = char
        valid = True
    else:
        valid = False

if valid:
    print("This is a valid file!")
else:
    print("This is not a PDF file...")