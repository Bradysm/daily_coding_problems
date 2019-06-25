# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.
# Example 2:
#
# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
#
# It doesn't matter what values are set beyond the returned length.

# the key to this problem is realizing that we can modify the array in place
# once we realize that we can do that, we can act like the array is split
# into two pieces. Everything from zero up to last is contained within
# the non-duplicate sorted array. What we can then do is start at position
# i and iterate over all of the numbers at each index to the right of that
# which are also equal to nums[i]. As we iterate over these numbers,
# We're indirectly getting rid of them because we never move the i ptr
# backwards. We then set the value of nums[last] = nums[i] to update the
# one copy that we needed into the non-duplicate array. We aren't worried
# about overwriting a value that we need because last is guaranteed to be <= i
# where the only values that are important to us from there on forward are
# >= i. At the end of this algo, last will contain the length of the sorted
# non-duplicate array because it's always set to store the next value,
# meaning it's one greater than the last stored index, or in other words,
# equal to the length.

def removeDuplicates(self, nums: List[int]) -> int:
    last = i = 0 # assume the initial length is zero
    len_nums = len(nums)
    while i < len_nums:
        nxt = i+ 1
        # move over duplicates
        while nxt < len_nums and nums[i] == nums[nxt]:
            nxt += 1
        # move the value to last
        nums[last] = nums[i]
        last += 1  # increment for next index
        i = nxt
    return last