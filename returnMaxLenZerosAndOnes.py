# given a binary array, return the max length of contiguous zeros and ones in the array
# capital one

# So Immediately when I saw this problem, I thought of the O(n) solution. I don't know if this
# is a testament to practice, but I realized that you want to almost converge in from the left
# and the right. Although I initially tried building from the left and incrementing the right
# I realized that we more so want to move in, instead of moving outwards. Then, when  you find
# the same numbers of ones and zeros between the two you return that number, else you 
# try to remove from the left if that's the correct removal, and if that's not the correct removal, 
# then greedily remove from the right. The key is to decrement the count from the number
# at that index, then continue moving forward.

# lastly, we keep looping as long as left is < right, the reason being is that there will never
# be and equal number of 1's and 0's if they're also the same index, so that's why it's
# not <=

# great! O(n) time and O(1) space!! CHEERS BRADY

def max_len_zeros_and_ones(nums):
    zeros = 0
    ones = 0

    # get the counts of all of them
    for num in nums:
        if num: ones += 1
        else: zeros += 1

    # set the pointsers
    left = 0
    right = len(nums) - 1

    # move inwards and act greedy on removal
    while left < right:
        if zeros == ones:
            return zeros + ones
        # more zeros than ones
        if ones < zeros and nums[left] == 0:
            zeros -= 1
            left +=1
        elif zeros < ones and nums[left] == 1:
            ones -= 1
            left += 1
        else: # remove the right
            if left[nums]: ones -= 1
            else: zeros -= 1
            right -= 1

    return 0


print(max_len_zeros_and_ones([0, 0, 0, 1, 1, 0, 0, 1 , 1, 0]))
print(max_len_zeros_and_ones([0, 0, 0, 1]))
print(max_len_zeros_and_ones([0, 0, 1, 0, 0, 1 , 1, 0]))
print(max_len_zeros_and_ones([0, 1]))
print(max_len_zeros_and_ones([0]))
print(max_len_zeros_and_ones([]))
print(max_len_zeros_and_ones([0, 0, 1, 1, 0, 0, 1 , 1, 0]))