# Good morning! Here's your coding interview problem for today.
# This problem was asked by LinkedIn.
# Given a list of points, a central point, and an integer k, find the nearest k points from the central point.
# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)]

# so when you see the k closest or k smallest, you want to think of a heap right away
# this will then allow us to find the closest points to the center using the distance 
# formula with the points that are given to us

# also notice the way that I use the heap:
# we use negative because we want to keep the closest values, so the larger ones
# we want to treat as being smaller, so we turn them negative so they get popped off first

# Also, you need to know the distance formula to solve this problem. I simply assume that this is know prior to
# attempting this solution

# my solution is O(n*log(k)) and O(k) space; since k can grow to the size of n, we must include it in the time
# comlpexity because it can grow to inifity with n

import heapq
from math import sqrt
def k_closest_points(points, cpoint, k):
    k_nearest = []
    cx, cy = cpoint # deconstruct the central point
    for point in points: # O(n)
        px, py = point  # deconstruct each point
        distance = sqrt(pow(px-cx, 2.0) + pow(py-cy, 2.0))

        # check to see if we don't have k already
        # insertion into the heap is log(k)
        if len(k_nearest) < k: 
            heapq.heappush(k_nearest, (-1 * distance, point))
        else: 
            heapq.heappushpop(k_nearest, (-1 * distance, point))

    return [point for _, point in k_nearest]


print(k_closest_points([(0, 0), (5, 4), (3, 1), (100, 1), (1, 2)], (1, 2), 2))

