# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# Right when I saw this problem I knew somewhat what I needed to do. The main thing was the concept
# that I needed to recognize, this is the TWO POINTER TECHNIQUE. The biggest thing to recognize
# is that when you get to a number in the array, you need to swap that number
# with the first zero that occurs in the array BEFORE it. You then need to have a pointer
# for the zero and for the first zero before it and for the index that you're moving down the array
# 
#  Watch and see how I do it below

def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def move_zeros(nums):
    first_prev_zero = -1 # we haven't seen a zero
    for i in range(len(nums)):
        if first_prev_zero == -1 and nums[i] == 0:
            first_prev_zero = i # set the first previous zero
        if not first_prev_zero == -1 and nums[i]:
            swap(first_prev_zero, i, nums)
            next_zero = first_prev_zero + 1 # the next potential zero will be the location after the swap
            first_prev_zero = -1 if next_zero == len(nums) or nums[next_zero] is not 0 else next_zero
    
    return nums
        
test_arr = [0,1,0,3,12]
test_arr2 = [0, 0, 4, 6, 0, 1, 0, 0, 7, 9]
print(move_zeros(test_arr))
print(move_zeros(test_arr2))