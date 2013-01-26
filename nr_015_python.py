#########################################
# Problem Nr. 15
# Starting in the top left corner of a 2x2 grid,
# there are 6 routes (without backtracking) to
# the bottom right corner.
#
# How many routes are there through a 20x20 grid?
#########################################

#based on combinatorics (maybe a little bit of cheating ^_^)

from math import factorial
grid_size = 20

routes = factorial(grid_size * 2) / (factorial(grid_size) * factorial(grid_size))
print routes