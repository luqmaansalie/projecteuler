
# https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

a = 0
for i in range(999, 908, -1):

	for j in range(999, 100, -1):
		x = str(i*j)
		y = i*j

		if x == x[::-1] and y > a:
			a = y
print(a)
