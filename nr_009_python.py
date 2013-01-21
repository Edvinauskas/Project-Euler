#########################################
# Problem Nr. 9
# A Pythagorean triplet is a set of
# three natural numbers, a  b  c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean
# triplet for which a + b + c = 1000.
# Find the product abc.
#########################################
import math

def find_pyth(n): #Added a function so when its found, no more work is needed
    for a in range(1, n):
        for b in range(a, n):
            if (a + b + (math.sqrt(a**2 + b**2))) == n:
                return int(a * b * math.sqrt((a**2 + b**2)))

print find_pyth(1000)
