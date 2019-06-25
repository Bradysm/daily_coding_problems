# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

# this problem is painfully easy if you know some simple math formulas off the top of your head
# because they provide us with the fact that we're given n numbers from the range 0-n
# and we need to find the one number that is missing, we can simply use the formual to calculate
# the sum from 1-n, which is the sum from 0-n, and then subtract the running sum within numbers
# from that. You will then get the number that is missing.


def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    total = n * (n + 1) / 2
    return int(total - sum(nums))
