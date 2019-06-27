# given an array of numbers, return the longest range contained within the numbers
# ex) [1, 10, 8, 15, 0, 5, 12, 14, 16, 2, 4, 3, 11, 13, 9], the longest range here would be [0, 5]

# the most obvious solution is to sort the list and then find the 
# longest range using two pointers. This works great, but we're bottlenecked at O(nlogn)
# complexity. Can we do better?

# it just so happens that we can. What if we could access all of the numbers
# immediately, and then iterated from the smallest number until the largest number
# in the array. this would be O(n + k) where k is the distance from the smallest
# number to the largest number. This would also take O(n) space but would
# be much faster than O(nlogn)
import sys

def longest_range(nums):
    seen = set(nums)
    min_val = min(nums)
    max_val = max(nums)

    # iterate through the range
    rng = [-1, -1]
    val = min_val
    begin = None
    cnt = 0
    while val <= max_val:
        if val in seen:
            if begin is None: begin = val # not in
            else: cnt += 1  # increment the range count
        else: # not seen
            begin = None
            cnt = 0
        # check if we update the range
        if begin is not None: # we found some range
            if (cnt+1) > (rng[1] - rng[0]):
                rng[0] = begin
                rng[1] = begin + cnt
        val += 1
    # return the range
    return rng


test_nums = [1, 10, 8, 0, 5, 2, 4, 3]
test_nums2 = [1, 10, 8, 15, 0, 5, 12, 14, 16, 2, 4, 3, 11, 13, 9]

print(longest_range(test_nums))
print(longest_range(test_nums2))