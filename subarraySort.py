# This is a problem that I absolutely love. It was defined as a hard problem on AlgoExpert, and I can't
# help but enjoy the math and cleverness behind the algorithm that I created.

# the question is:
# Write a function that takes in an array of integers of length at least 2. 
# The function should return an array of the starting and ending indices of the smallest 
# subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted. 
# If the input array is already sorted, the function should return [-1, -1].

# Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
# output: [3, 9]


# Okay, so let's first look at what it means to be sorted. For a number to be sorted, it must be greater
# than all of the numbers before it in the list, and less than all the numbers after it in the list. So I want you
# to notice two things: 1) if a number is unsorted, then there must be two numbers in the array that are unsorted
# 2) One number that is out of order could mean that it needs to be shifted far away from where it currently is, thus
# one  number could create a large subarray that needs to be sorted i.e. [1, 3, 4, 5, -1], notice that the 
# value returned for this array is [0, 4] because technically all of the numbers are not in sorted order due to
# not all the numbers before -1 being less than -1 and vice versa for all other numbers in the array.

# Okay, so how can we go about solving it?
# What we need to do is find the largest number that is unsorted and find it's sorted position, and then find
# the smallest number that is unsroted and get it's positon

# THere are a few ways that this can be done, but I chose to do it a bit of a sneaky way and I'll walk you through
# why and how it works.

# So, like I said the number in the array that we're currently at must be > the number than all the numbers to the left
# of it and it must be less than all the numbers to the right of it
# so, we can create a curr_max and iterate from left -> right through the array, if the current number is < the current 
# max, that means that there is a number to the left of it that is greater than that number, so we update the leftbound
# index to that index and update curr_max by using <- max(curr_max, num). This will eventually find the rightmost index
# that the greatest number out of place needs to be placed in. 
# 
# 
# We then do this from right to left, using a curr_min
# we check to see if the number in the iteration (from right to left in the array) is < curr_min. The reason
# we use current min is because we're using the current min of the max numbers. Just like finding the kth greatest
# number you would use a min heap .... (sorry went off on a tangent). Okay, so if the number is greater than current
# min, then there is a number to teh right of it that needs to be moved to that index or an index to the left of it.
# we then update the left range and make it equal to that index. curr_min <- min(curr_min, num). The left bound index
# continues to get updated to the index where the smallest number out of order will go. This is done by continueally
# checking if the smallest number before that number is less than the current number.

# okay, so, if we simply make two passes through this array, it will be O(n) time and O(1) space because we don't use an array
# (it will be helpful to create two arrays and follow the current_max and min from left to right and right to left respectively
# to get a greater understanding for how this works).

def subarraySort(array):
    upper = find_upper(array)
	lower = find_lower(array)
	return [lower, upper]
	
def find_upper(nums):
	# get the location of where the greatest unsorted number goes
	upper_i = -1
	curr_max = nums[0] # use a continuous max to find largest num out of order
	for i in range(1, len(nums)):
		num = nums[i] # get the current number and check to make sure in range
		if curr_max > num:
			upper_i = i
		curr_max = max(curr_max, num)
	return upper_i
	
def find_lower(nums):
	lower_i = -1
	curr_min = nums[len(nums)-1] # use continuous min to find smallest min out of order
	for i in range(len(nums)-2, -1, -1):
		num = nums[i]
		if num > curr_min:
			lower_i = i
		curr_min = min(curr_min, num)
	return lower_i
	



