multi_sum = 0
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        multi_sum += n

print multi_sum