# given two non empty arrays, THe function should find the pair of numbers (one from the first array and second array) whose absolute difference
# is the closest to zero and return them as an array. First index from first array, second from second array

# This solution runs in O(mlogm + nlogm) time and O(1) space
# will complete explination tomorrow

from bisect import bisect_right
import sys

def smallestDifference(arrayOne, arrayTwo):
	arrayTwo.sort() # mlogm
	arr = None
	diff = sys.maxsize
	for num in arrayOne: #nlogm
		i = bisect_right(arrayTwo, num) # find index to insert
		for di in [-1, 0]: # check current index and left one
			inRange = i+di in range(0, len(arrayTwo))
			if inRange and abs(num - arrayTwo[i+di]) < diff:
				arr = [num, arrayTwo[i+di]]
				diff = abs(num - arrayTwo[i+di])
	return arr