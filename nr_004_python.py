#########################################
# Problem Nr. 4
# A palindromic number reads the same both
# ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91  99.
#
# Find the largest palindrome made from the
# product of two 3-digit numbers.
#########################################

largest_palindrome = 0
for i in range(100, 999):
    for j in range(100, 999):
        palindrome = i * j
        if str(palindrome) == str(palindrome)[::-1]:
            if palindrome > largest_palindrome:
                largest_palindrome = palindrome

print largest_palindrome
