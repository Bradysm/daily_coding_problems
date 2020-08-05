"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase.
 You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

def staircase(n):
  # Fill this in.
  
print staircase(4)
# 5
print staircase(5)
# 8

Can you find a solution in O(n) time?


So this is A CLASSIC
Let's first solve this recursively and then get to the O(n) time. This is very similar to the fib
problem. If not, exactly like it.

So, here we can think we start at the nth stair, and the ways to get to the nth stair are the ways
to get to the n-2 stair and n-1 stair. We can then see that there are two base cases. When n=1, there
is one way to get up that stair and when n=2, there are two ways to get up teh stair.

Once we have that, we can see that we can actually start form the bottom and build up the solution
because we need the n-1 and n-2 number to get the nth number, just like fib right. So start at the
1 and 2 and then build up from there! Let's do it!

O(n) time and space

"""

def recursive_stair(n) -> int:
    # base cases
    if n <= 0: return 0
    if n == 1: return 1
    if n == 2: return 2

    return recursive_stair(n-2) + recursive_stair(n-1)


print("5 steps", recursive_stair(5))
print("4 steps", recursive_stair(4))
print("27 steps", recursive_stair(27))


def iterative_stair(n) -> int:
    if n <= 0: return 0

    # build an array to hold the numbers
    ways_to_climb = [0 for i in range(n+1)] # note that we have to do n+1 to make sure we can store the nth value
    ways_to_climb[1] = 1 # set the base cases to build up the soltion
    ways_to_climb[2] = 2

    for stair in range(3, n+1):
        ways_to_climb[stair] = ways_to_climb[stair-2] + ways_to_climb[stair-1]

    return ways_to_climb[n]


print("5 steps", iterative_stair(5))
print("4 steps", iterative_stair(4))
print("27 steps", iterative_stair(27))


"""
We can then see that we can just use two variables to store the
values instead of using an array to store the values

O(n) time O(1) space
"""
def iterative_stair_no_space(n) -> int:
    if n <= 0: return 0
    if n == 1: return 1
    if n == 2: return 2

    one_lower = 2 # act like this is the second stair
    two_lower = 1 # act like this is the first stair

    for stiar in range(3, n):
        ways_to_climb_stair = one_lower + two_lower

        # update the variables
        two_lower = one_lower
        one_lower = ways_to_climb_stair

    return two_lower + one_lower
    
print("5 steps", iterative_stair_no_space(5))
print("4 steps", iterative_stair_no_space(4))
print("27 steps", iterative_stair_no_space(27))