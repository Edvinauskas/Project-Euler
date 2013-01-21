#########################################
# Problem Nr. 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#########################################

import math

def is_prime(n):
    if n % 2 == 0:
        return False
    n_sqrt = int(round(math.sqrt(n)))
    for i in range(3, n_sqrt + 1, 2):
        if n % i == 0:
            return False
    return True

prime_sum = 2
i = 3
while i < 2000000:
    if is_prime(i):
        prime_sum += i
    i += 1

print prime_sum