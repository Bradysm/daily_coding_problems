"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a circular array, compute its maximum subarray sum in O(n) time. 
A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.


Okay, so i've seen the problem where you have to find the max subarray, and that problem
you simply decide whether it will be more beneficial for me to take the current number and
add it to my running sum, or if we should move on and start back at 0 and start a new sum.
For this you simply walk down the array, take the max of adding the number to our running
sum and 0. The reason we choose zero, is that at any point if we dip below zero in the sum,
it's no longer beneficial for us to include that previous subsequence. For this problem, I ran into
that issue.

So for this problem, I saw it almost as the inverse of the previous problem. The reason being, is that in
the circular array you can start at any point and wrap around to that point. That's not the issue. The issue
is when do we want to stop wrapping around. Where exactly do I cut off the sequence to say that I don't want
to add any more numbers. For this, I started looking more into the problem. I realized that we really are looking
to remove the most negative subsequence from the total sum. The reason being that we take the total sum is
that the array is circular, so we can start at any point and rotate back to the front, but we want to remove
the MOST NEGATIVE SEQUENCE to give us the max positive sequence of numbers from the array. If there are no negative
numbers, then we just subtract 0 from the total, otherwise, we simply remove the most negative sequence. This allows
us to tackle the issue that we found before where we might actually want to inlcude a negative number in our sequence
because it might lead to a future reward that will negate the small negative charge currently.

This algorithm will make two passes so it will perform in O(n) time
- one pass to create the total sum, one pass to find the most negative subsequence and remove it from the sum
"""

def circular_max_subarray(nums) -> int:
    total_sum = sum(nums)

    # max of the negative subarray
    

    # find the maximum negative subarray
    left = 0
    right = 0

    max_negative_subarray = 0
    curr_negative_subarray = nums[left] if nums else 0
    while left < len(nums):
        # check to see if right is less than left
        if right < left: 
            right = left - 1
            curr_negative_subarray = 0
        
        # check to see if we should add the next number
        next_num = nums[(right + 1) % len(nums)]
        if curr_negative_subarray +  next_num < 0:
            curr_negative_subarray += next_num
            right += 1
        else: # we shouldn't add it, move left up
            curr_negative_subarray -= nums[left]
            left += 1

        max_negative_subarray = min(max_negative_subarray, curr_negative_subarray)
        
    """
    for i, num in enumerate(nums):
        # decide if we should add the current number
        curr_negative_subarray = min(0, num + curr_negative_subarray)
        max_negative_subarray = min(max_negative_subarray, curr_negative_subarray)

        15
6
23
13
15
5
    """

    # subtract the max negative subarray from the total sum
    return total_sum - max_negative_subarray


print(circular_max_subarray([8, -1, 3, 4]))
print(circular_max_subarray([-4, 5, 1, 0]))
print(circular_max_subarray([10, -4, -8, 5,  8, 1, 0, -1]))
print(circular_max_subarray([-11, 10, -4, -8, 5,  8, 1, 0, -1])) # should return 13, because adding 10 is no longer beneficial
print(circular_max_subarray([10, -4, -8, 5,  8, -8, 1, 0, -1])) # should return 15, because we start at five and wrap to 10
print(circular_max_subarray([-11, 10, -4, -8, 5,  8, -8, 1, 0, -1])) # should return 15, because we start at five and wrap to 10
