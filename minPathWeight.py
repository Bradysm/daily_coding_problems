#Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.


# this problem has a very easy solution that you can think of from acting recursively
# there is only two ways to go, so given some point x,y we will act both ways and
# then return the min value for both directions. This will act recursively and will
# have a O(2^n) runtime because each node in the tree has two directions to go
# we can save some time with this by using a 2D array along with it and
# tracking values that we already computed. This will save on runtime, but will
# add the O(m*n) space to the space already needed on the stack for recursive calls.

# what if we could think in a DP standpoint and act optimally from a sub problem
# so starting at the endpoint, there is nowhere to go so we keep the value
# at that index. We then move to the left, we take the min of the
# element to the right and down and add this to the current value at that index
# we keep doing this right to left, bottom to up adding the min of the 2 directions
# to each element. The reason we work left and up is because it's the opposite of the
# movements that we are given and we're working backwards from the end goal (get why it's reversed now)
# we continue this all the way to the starting point. Now, we can simply return the value at the
# starting point and you're good to go!!! This will have an O(m*n) runtime and will require no extra spaceß

import sys

def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m_sz = sys.maxsize
    rows = len(grid)
    cols = 0 if rows == 0 else len(grid[0])
    for row in reversed(range(rows)):
        for col in reversed(range(cols)):
            r = m_sz if col +1 >= cols else grid[row][col +1]
            d = m_sz if row +1 >= rows else grid[row +1][col]
            min_val = 0 if r == m_sz and d == m_sz else min(r, d)
            grid[row][col] += min_val

    # return the least weighted path
    return grid[0][0]