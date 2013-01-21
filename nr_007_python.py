#########################################
# Problem Nr. 7
# By listing the first six prime
# numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
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

prime_count = 1
i = 3
answer = 0
one_thousand_first = False

while not one_thousand_first:
    if is_prime(i):
        prime_count += 1
    if prime_count == 10001:
        one_thousand_first = True
        answer = i
    i += 1

print answer