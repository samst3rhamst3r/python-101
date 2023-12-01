# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

str_input = input("Please input a string of words: ")

symbol_input = ""
while len(symbol_input) < 1 or len(symbol_input) > 1:
    symbol_input = input("Please input one symbol to replace with: ")

new_str = str_input.replace(str_input[0], symbol_input)
print(new_str)