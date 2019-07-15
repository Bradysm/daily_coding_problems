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


# lets do even better! 
# to do this we will use a map. We will fill all the numnbers into a map and set the value to false
# The false means that we havent' checked over this number before. You will understand why we do this
# and don't just use a set when I explain it. THe first pass we create the map, the second pass we 
# move through the array and find the longest range. WHat we do there is start at the number and 
# check to see if there are numbers before it and numbers after it that belong in the range. 
# when we do this, we check in the map. We want to turn the value to true when we visit that value
# so we don't try to iterate over that range again. The reason I say this is that imagine the input
# was a sorted array that was also filled with consecutive numbers. Then we would check over it n^2 times
# if we didn't store whether we saw that value yet or not. We really don't want to do this. If we've seen
# the value, MOVE ON, Kapeesh. Good. We have the algo let's get it together

def expand_range(num: int, visited_nums: dict) -> int: 
    curr_range = 1 # just counting the current number
    val = num - 1
    while val in visited_nums and not visited_nums[val]:
        curr_range += 1
        visited_nums[val] = True # visit the value
        val -= 1
    val = num + 1
    while val in visited_nums and not visited_nums[val]:
        curr_range += 1
        visited_nums[val] = True # visit the value
        val += 1
    return curr_range


def longest_range_fast(nums) -> int:
    visited_num = {n : False for n in nums} # create the map
    longest_range = 0
    for n in nums:
        if not  visited_num[n]: # check to make sure we haven't visited it
            longest_range = max(longest_range, expand_range(n, visited_num))

    return longest_range


print(longest_range_fast(test_nums))
print(longest_range_fast(test_nums2))