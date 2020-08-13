"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a number like 159, add the digits repeatedly until you get a single number.

For instance, 1 + 5 + 9 = 15.
1 + 5 = 6.

So the answer is 6.


THOUGHT PROCESS:
What we're essentially going to be doing is, we want to be able to sum the digits of a number
and then check to see if that number is a single digit or not (we can) check to see if dividing
by 10 is greater than 0. Then we want to continue doing this until dividing by 10 is equal to zero.
"""


def add_digits(n) -> int:
    summed_digits = n
    while summed_digits // 10 > 0:
        # not a single digit
        summed_digits = _sum_digits(summed_digits) 
    
    return summed_digits


def _sum_digits(n) -> int:
    num = 0
    while n:
        digit = n % 10
        num += digit
        n //= 10

    return num


print(add_digits(159))