# this is a very common problem that is used in coding interviews.
# instead of asking this problem directly, they will add some twists into
# the question, but for the most part, the problems will involve you deciding
# whether to include something in a set or list, and then validating if that
# set fits within the valid sets

# the way to think of this problem is to start with an empty set, or empty list
# and then move down the array, and at each index, choose to either add the number
# into the set or to exclude it. We have then identified the sub problem within the problem
# which will allow us to create a recursive solution to the problem
from copy import deepcopy

def powerset(nums):
    """
    returns the powerset of the set nums. Length of the powerset it 2^n
    :param nums: numbers within the original set
    :return: array containing arrays representing sets
    """
    p = []
    pset_help(nums, p, [], 0)
    return p


def pset_help(nums, pset, currs, i):
    """
    helper function used to generate the powerset
    :param nums: list of original set
    :param pset: list for powerset
    :param currs: list containing the current set
    :param i: current index
    :return: None
    """
    if i == len(nums):
        pset.append(deepcopy(currs))
        return  # reached the end of the array
    pset_help(nums, pset, deepcopy(currs), i+1)  # dont include it
    currs.append(nums[i])
    pset_help(nums, pset, deepcopy(currs), i+1)


print(powerset([1,3,5]))




def d_pset(nums):
    """
    creates the powerset using dynamic programming
    This will work by working our way down to the end
    of the array, and then working back up recursively
    :param nums: current set of numbers
    :return: list containing the powerset of nums
    """
    return d_pset_help(nums, 0)

def d_pset_help(nums, i):
    # check to
    if i == len(nums):
        return [[]] # creates a list containing an empty list
    pset = []
    for s in d_pset_help(nums, i+1):
        pset.append(deepcopy(s))
        s.append(nums[i])
        pset.append(deepcopy(s))
    return pset


print(d_pset([1,3,5]))



