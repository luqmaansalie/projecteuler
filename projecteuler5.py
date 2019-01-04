
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

constant = 1
factor = 0

for i in range(2, 20):
    if isPrime(i):
        constant *= i

all = False

while not all:
    all = True
    factor += constant

    for i in range(11, 21):
        if factor % i != 0:
            all = False
            break

print(factor)
