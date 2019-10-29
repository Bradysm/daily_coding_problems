# Good morning! Here's your coding interview problem for today.
# Given a real number n, find the square root of n. For example, given n = 9, return 3.

# Okay, so before we tackle this problem, let's first understand what is going on
# we're asked to give the square root of some number n. Now, there are built in libraries 
# to do something like this, but I don't think that's what  they're looking for. So, 
# instead, let's look at what a square root of a number n is.

# so if we start with some number n the square root of the number n is some real number a such that
# a*a = n. So, if we then move this around, it's also valid to say that a = n/a. We can then
# change it to say as well that c is a square root of n if there is some number b that divides
# n such that c == b. We then can undertand that the range of possibilities for the square root
# of sum real number n, is between 0 and n. So, naively we can go through zero -> and increment
# the counter until we get to n. This will work great for square roots that are integers,
# but what if they're floating point values?!?! There are infinity floating point numbers
# between 0 -> 1, oh lord, we're in for one brady.

# well fear not, we can still do this and ill show you how. Lets say we pick a number b that
# is between 0 and n, let's just say it's n/2 for now. We then divide n by b and get some
# number c. Knowing what we said before, if b is < c, then that means that the potential
# square root that we chose is too small, because the quotient is actually larger than
# the number that we chose. If b > c then that means that we chose a number too large.
# so knowing this, we can then discard all numbers greater than or equal to b, because 
# they too will be too large (and vice versa for the previous example). We then
# cut our search range in half, and then continue doing this cut in half until we find
# a b that is equal to c. 

# okay, that is great and all Brady, but how do we do the comparisons for floating points?
# So, we can subtract the two numbers and then check to see if the absolute difference betweeen
# the two numbers is less than some epsilon that we define. We can then set this epsilon
# to a very tiny number, meaning the two doubles must be extremly close to eachother in value.

# BOOM, we've just moved from an O(n) solution to an O(logn) solution. Fantastic!
# Until next time!

# Cheers, Brady


def find_sqrt(n):
    epsilon = 0.0000001
    left = 0
    right = n
    # continue if left is less than or equal to right
    while left < right or abs(left-right) < epsilon:
        sqrt = left + (right - left) / 2
        quotient = n if not sqrt else n / sqrt
        if abs(sqrt-quotient) < epsilon:
            # return the value rounded to the fourth digit
            return round(sqrt, 4) 
        elif sqrt < quotient:
            left = sqrt + epsilon
        else: # sqrt is greater than quotient
            right = sqrt - epsilon
    
    return -1



print('finding the sqrt of 9: {x}'.format(x= find_sqrt(9)))
print('finding the sqrt of 1: {x}'.format(x= find_sqrt(1)))
print('finding the sqrt of 7: {x}'.format(x= find_sqrt(7)))