# This problem was asked by Facebook.
#
# Given an array of integers, write a function to determine whether the array could
# become non-decreasing by modifying at most 1 element.
#
# For example, given the array [10, 5, 7], you should return true,
# since we can modify the 10 into a 1 to make the array non-decreasing.
#
# Given the array [10, 5, 1], you should return false,
# since we can't modify any one element to get a non-decreasing array.


# Notes to myself: If the array is non-decreasing that means that it must
# be increasing from the left to the right, but DECREASING from the right to the left

# if we can move from right to left and then check to see if the value before the current
# value is less than OR EQUAL TO the current number, then we can move on.
# Note that using negation we get less than or equal to because it's not decreasing
# by staying stagnant.

# If the value is not, mark it as needed to be changed, but don't change it
# then if we get to a point where need to be changed is 1, and we have to change another
# return False, other wise return true

def nondecreasing(arr):
    """
    Checks to see if the array given is non-decreasing or if one
    Value can be changed that will make it non-decreasing
    :param arr: array of numbers
    :return: True if 0 or 1 element needs to be changed
    """
    changed = 0
    for i in reversed(range(1, len(arr))):
        if arr[i-1] > arr[i]:
            changed += 1  # mark the element as needed to be changed
            if changed > 1: return False
    return True


# check to make sure that it's working
print(nondecreasing([10, 5, 7]))  # should be true
print(nondecreasing([10, 5, 1]))  # should be false
print(nondecreasing([1, 8, 10, 7, 12]))  # should be true
print(nondecreasing([19, 2, 7, 8, 1]))  # should be false
print(nondecreasing([19, 2, 7, 8, 21]))  # should be true
