#########################################
# Problem Nr. 6
# The sum of the squares of the first ten
# natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten
# natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of
# the squares of the first ten natural numbers
# and the square of the sum is 3025  385 = 2640.
#
# Find the difference between the sum of the
# squares of the first one hundred natural
# numbers and the square of the sum.
#########################################

first_square_num = 0
second_square_num = 0

for i in range(1, 101):
    first_square_num += i**2

for i in range(1, 101):
    second_square_num += i

print (second_square_num**2) - first_square_num