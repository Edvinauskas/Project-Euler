#########################################
# Problem Nr. 5
# 2520 is the smallest number that can be
# divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that
# is evenly divisible by all of the
# numbers from 1 to 20?
#########################################

divisible = False
number = 0
while not divisible:
    divisible = True
    number += 20
    for denom in range(1, 21):
        if number % denom != 0:
            divisible = False
            break
    if divisible is not False:
        divisible = True

print number

