# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
# implement a function rand5() that returns an integer from 1 to 5 (inclusive)

# lets talk about how I came up with this answer
# first, you need to understand how we come up with probability
# So generic undersating of probability is needed to do this problem
# Since we want to have an even distribution of numbers produced from rand5
# we want to make sure that 1-5, each number has a 20% chance of being picked
# Since we're given a function that has a uniform probability distribution
# from 1-7, we need to "shrink" that distribtuion back down to 1-5. So,
# how can we do this? Well first we can think about "extending" the range
# of numbers that are being produced as a multiple of 5. So we will
# take the random function and multiply it by 5, so 1-5 would represent
# the choice of 1 from rand7 etc etc. Once we have this, we will be producing
# numbers 1-35. We need to then tranform this to 1-5. To do this, you should
# immediately think of using the mod function. But wait Brady, this will
# produce the numbers 0-4!!!!!

# stay patient, all you have to do is add 1, and now the output range will be
# between 1-5!!!! so if you enumerate all of the probabilities, each number
# 1-5 will show up 7 times from the mapping that we created, thus each number
# has a probability of 7/35 or 1/5 which is 20%!!! There you go. Ez pz.

def rand5(rand7):
    return ((rand7() * 5) % 5) + 1

