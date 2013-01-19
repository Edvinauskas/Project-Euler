largest_prime = 0
prime_fac = 600851475143
num = 0

while num < prime_fac:
    num += 1
    if prime_fac % num == 0:
        largest_prime = num
        prime_fac = prime_fac / num

print largest_prime