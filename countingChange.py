# given and infinite number of quarters, dimes, knickles, and pennies; Count the number
# of ways to represent n cents

# this is a classic DP problem. The second you see "count the number of ways.." You want
# to think of DP and/or recursion. When I first saw this problem, I had already done a bunch
# of DP so I decided to start with creating an extra array and defining the relation of
# the ith ways of counting change. So in this "cents" we be building up the solution.

# think about it like this. The number of ways to count 0 cents in change is zero because there
# is one way to count zero cents. Lets say we want to count the number of ways to count 2 cents.
# Lets first try to take a coin from each of our categories and then find the number of ways
# to count i - (coin value) cents. So if I put a penny down, then I would need to find the
# number of ways to count 1 cent. Now lets try to take a quarter and put it down. Well
# this would mean the person would now owe you 23 cents, so this is not good. you could have
# -23 to count from, so just return zero because that is not a viable option. We then continue
# doing this until we get to the nth index and voila, you have the number of ways to count
# n cents.

# so, you're probably asking, can't we just make a recursive solution and call it a day?
# sure, get O(3^n) time complexity and O(n) space for the recursive calls! That doesn't
# sound too good, but if you need to initially start the ball rolling in an interview,
# it will never hurt to give that brute force solution and then try to make it more refined
# it might help you see that the ith cent only relies on calculating how to count the
# i-25, i-10, i-5, and i-1 cent value. Also note, you could speed up the recursive
# brute force solution by using memoization to get the relation.

def count_cents(n):
    """
    This function counts the number of ways to make n cents in change
    :param n: the cent value
    :return: int representing the number of cents in change created
    """
    counts = [0] * (n+1)  # note we do n+1 to make space for zero
    counts[0] = 1  # set the zero'th place to 1
    # for every coin
    for cent in [1, 5, 10, 20]:
        # add increment the number of ways to count i coins by the number of ways to
        # count i-cent. Only choose the numbers in the range from that cent forward
        for i in range(cent, n + 1):
            counts[i] += counts[i-cent]
    return counts[n]


# print out the value
print(count_cents(7))
print(count_cents(12))

