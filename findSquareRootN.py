"""
Good morning! Here's your coding interview problem for today.

Given a real number n, find the square root of n. For example, given n = 9, return 3.


Essentially, what we're going to do, is see if we can binary search for this number
so the way im going to look at it, is we're given a range from 0 to N, and we need
to find the number between here that when multiplied by itself gives us N. We can
then binary search for this number and find the square root in O(logn) time where n
is the number of integers from 0 to N
"""
from math import isclose


def find_square_root(n) -> float:
    low = 0
    high = n

    while low <= high:
        # get the median of the two numbers and then square it
        median = (low + high) / 2.0
        squared_median = median**2

        # check to see how close we are to n
        if isclose(n, squared_median, abs_tol=0.0003): 
            return round(median, 3)
        elif squared_median < n: # if the current square is less than n, then don't worry about numbers smaller
            low = median
        else: # the squared median was too big, cut in half those numbers
            high = median


# testing values
print(find_square_root(9))
print(find_square_root(15))
print(find_square_root(81))
print(find_square_root(144))
print(find_square_root(181))