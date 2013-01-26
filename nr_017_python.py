#########################################
# Problem Nr. 17
# If the numbers 1 to 5 are written out in
# words: one, two, three, four, five, then
# there are 3 + 3 + 5 + 4 + 4 = 19 letters
# used in total.
#
# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many
# letters would be used?
#
# NOTE: Do not count spaces or hyphens. For
# example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when
# writing out numbers is in compliance with British usage.
#########################################

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundred = ["hundred"]

def numbers_to_words(num):
    in_words = []
    num_int = [int(i) for i in str(num)][::-1]
    print num_int
    if num < 10:
        return ones[num]
    i = 1
    for i in range(1, len(num_int)):
        if num_int[i] == 1 and num_int[i - 1] != 0:
            in_words.append(teens[num_int[i - 1]])
        else:
            in_words.append(tens[i])
    return in_words

letter_count = 0
for i in range(1, 25):
    written_out = numbers_to_words(i)
    letter_count += len(written_out)
    print written_out

print letter_count