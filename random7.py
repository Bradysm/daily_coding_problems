# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
# implement a function rand5() that returns an integer from 1 to 5 (inclusive)

# this problem is not very challenging because they give us a range that is greater
# than the range that we are trying to land within.
# we simply need to generate a number, using rand7, this will give us a number between
# 1-7, if the number is greater than 5, then we will simply discard the value
# and try again. Technically in the worst case this will never happen, but the probability
# of hitting 6 or 7 consistently forever is almost zero. This acts like rejection sampling
# in AI. I have provided a test that you can run. The numbers fluctuate ~ +/-15 from 200.
# thus empirically proving the uniform distribution.


import random
from collections import Counter


def rand7():
    return random.randint(1, 7)


def rand5(rand7):
    num = rand7()
    while num > 5:
        num = rand7()
    return num


# test to make sure it's working
c = Counter()
for n in range(1000):
    c[rand5(rand7)] += 1

# print the number of times the number showed
for k, v in c.items():
    print(k, v)



