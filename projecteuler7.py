
# https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

a = 4
s = 0

i1 = 11
i3 = 13
i7 = 17
i9 = 19

while a < 10001:
	if isPrime(i1):
		a += 1
		s = i1
		if a == 10001:
			break

	if isPrime(i3):
		a += 1
		s = i3
		if a == 10001:
			break

	if isPrime(i7):
		a += 1
		s = i7
		if a == 10001:
			break

	if isPrime(i9):
		a += 1
		s = i9
		if a == 10001:
			break
	
	i1 += 10
	i3 += 10
	i7 += 10
	i9 += 10

print(s)
