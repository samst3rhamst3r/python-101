# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

user_in = input("Please type in any words or characters: ")

for vowel in "aeiou":
    count = user_in.count(vowel)
    print(f"\"{vowel}\" appeared {count} times")