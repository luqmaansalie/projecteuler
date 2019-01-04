
# https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def primeList(n):
	areprimes = [True] * n
	total = 2
	
	for i in range(3, n+1,2):
		if areprimes[i] == True:
			total += i

			for j in range(i*i, n, i):
				areprimes[j] = False
	print(total)

primeList(2000000)
