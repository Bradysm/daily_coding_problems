# given a number n, return a list containing numbers 1 through n
# that is sorted lexiographically
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9]

# this problem is question 389 on leetcode
# my solution is faster than 93% of the other soltions

# I first realize that we're creating a list of numbers from 1-n, so I immediately
# think of using the range function with an initializer list to generate the numbers
# once we have the list of numbers, we then need to sort the numbers, using their
# lexiographical value. We can do this by using the built in sort function
# that is included within the list datastructure. If we used the sort algorithm
# with no arguments, then the numbers would be sorted numerically. This is not what we want
# Instead, we want to treat them as if they were strings. To do this, we change the key for
# sorting to the string representation of the number using a lambda expression. This will
# then result in the values being sorted in a lexiographical fashion but will maintain
# their numerical identity.

# viola. There you go, a simple, but useful solution.
# lastly, note that range is not inclusive on the ending value, so n+1 is used


def lexicalOrder(n):
    """
    :type n: int
    :rtype: List[int]
    """
    l = [x for x in range(1, n + 1)]
    l.sort(key=lambda v: str(v))
    return l

