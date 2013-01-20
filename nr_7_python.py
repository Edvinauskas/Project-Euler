#########################################
# Problem Nr. 7
# By listing the first six prime
# numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#########################################

find_prime = 10001
primes = []
number = 2
while len(primes) < find_prime:
    number += 1
    is_prime = True
    for i in range(2, len(primes)):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)

print primes[-1]