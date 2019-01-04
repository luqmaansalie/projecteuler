
# https://projecteuler.net/problem=9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

x = 0
for a in range(1, 1000):
    if x > 0:
        break

    for b in range(2, 1000):
        c = (a**2 + b**2)**0.5
        if (a + b + c == 1000):
            x = a*b*c
            break

print(x)
