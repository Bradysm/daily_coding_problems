# given a list of numbers, return the length of the longest increasing subsequence

# the way that I like to think about these problems is to think of bellman equations
# With these equations, you choose your current step based on fact that all previous
# steps were optimal, thus choosing the optimal step at the current step will ensure
# that your current path is acting optimally. You see this alot in Value iteration
# for AI (fun reading and I highly recommend you look into those topics)

# anyways, to start of this problem, I will be using just a simple 
# bellman like equation that has you act opitmally based on the previous
# calculated values. So we will keep stepping down the array recurisvely,
# and then build the values back from teh bottom up. This is more a naive
# solution and it will have a runtime of around O(2^n). The reason why
# it is roughly O(2^n) is because not every index in the array will
# have a branching of 2. If the current index is not greater than
# the previous value, then there is only one branch that is taken.
# there is also a O(n^2) solution that can be created using a bottom
# up appraoch. I will detail this at the bottom of the script

# for this solution, the best way to think about it is that you either
# choose to include the value if it's greater than the prev, and then
# you also choose to not inlcude it to see if that could produce a more
# optimal solution. If that doesnt make sense to you, think of [1, 100, 5, 6, 7]
# If you always choose to only add the value if it's increasing and never choose
# to not add it, you will get 2 instead of 4 for this test case. So it's important
# to almost think of it like a powerset and to choose to include it or not.

# notice for this solution we do not carry the whole sequence. For the next
# solution I will show why carrying the whole sequence might be a good idea for
# certain problems. For this problem, adding the ith number only relies on
# the i-1 value, thus we just need to maintain the i-1 value and not
# the whole sequence.

import sys

def longest_inc_sub(nums):
    if nums is None: return 0 # check for when the list is empty or null
    return lic_help(nums, -sys.maxsize, 0)

def lic_help(nums, prev, i):
    """
    nums: list of numbers
    prev: previous number added to the subsequence
    i: current index within the list
    """
    # check to see if we're at the end of the array
    if i == len(nums): return 0
    # take the longest of including the value and not including the value
    longest = -sys.maxsize if nums[i] <= prev else 1 + lic_help(nums, nums[i], i+1)
    return max(longest, lic_help(nums, prev, i+1))
    


# test to make sure it works
print('first test:')
t = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_inc_sub(t))
t = [1, 5, 2, 80, 6, 90, 10, 11]
print(longest_inc_sub(t))
t = [1, 100, 5, 6, 7]
print(longest_inc_sub(t))


# here is another interesting implementation
# for this problem, there is only n recursive calls
# but for each recursive call, there is a deep copy
# of all of the lists that were created up to that point
# in the worst case there are 2^n lists, and for each list
# of size k, there will be an O(k) deep copy thus making
# the time complexity O(n + 2^n*k). Although the time does
# not sound great at all, this would be a better algorithm
# for a problem that asked you to print out all the increasing
# subsequences within the given array. 

from copy import deepcopy
def lis(nums):
    return len(max(lis_h(nums, 0), key=lambda x: len(x)))

def lis_h(nums, i):
    if i == len(nums): return [[]]
    arr = []
    for seq in lis_h(nums, i+1):
        t = deepcopy(seq)
        arr.append(t)
        if len(seq) == 0 or (len(seq) > 0 and nums[i] < seq[-1]): # check to see if it's less than the last one
            seq.append(nums[i])
            arr.append(seq)
    return arr


print("\nsecond test:")
t = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(t))
t = [1, 5, 2, 80, 6, 90, 10, 11]
print(lis(t))
t = [1, 100, 5, 6, 7]
print(lis(t))


# here is the O(n^2) solutuon. This will used cached sequence value...