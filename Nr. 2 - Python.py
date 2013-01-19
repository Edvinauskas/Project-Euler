even_fib_sum = 0
first = 1
second = 1
while second < 4000000:
    first, second = second, (first + second)
    if second % 2 == 0:
        even_fib_sum += second

print even_fib_sum