# Print out every prime number between 1 and 1000.

import math

# Sieve of Eratosthenes algorithm
n = 1000
array = [True for i in range(n)]
array[0] = False # 1 is not a prime number

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i - 1]:
        j = i**2
        while j <= n:
            array[j - 1] = False
            j += i

for i in range(len(array)):
    if array[i]:
        print(i + 1)