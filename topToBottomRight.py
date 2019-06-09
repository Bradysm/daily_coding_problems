# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# There is an N by M matrix of zeroes.
# Given N and M, write a function to count the number of ways of starting at the top-left corner
# and getting to the bottom-right corner. You can only move right or down.
#
# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

# here is a simple brute force solution. I was a little confused if we were actually given the array
# of not, so I simply used the nxm matrix lengths that were given. Keep in mind that n is the number
# of rows in the matrix and m is the number of columns in the matrix. this will have an O(2^(mxn)) complexity
# obviously we can make this better, so present this general brute force solution to the interviewer and then
# get thinking again because we CAN AND WILL DO BETTER!

def calculate_paths(arr):
    """
    calculates the number of paths from the top left of a matrix to the bottom right
    :param n: rows in the matrix
    :param m: columns in the matrix
    :return: int representing the number of paths to the bottom right
    """
    return _c_p_help((0, 0), len(arr)-1, len(arr[0])-1)

def _c_p_help(pos, row, col):
    if pos[0] > col or pos[1] > row: return 0  # there is no more moves
    if pos == (col, row): return 1  # formulates one path
    return _c_p_help((pos[0] + 1, pos[1]), row, col) + _c_p_help((pos[0], pos[1] + 1), row, col)

def matrix(n, m):
    return [[0 for i in range(m)] for y in range(n)]


print(calculate_paths(matrix(2, 2)))  # should be 2
print(calculate_paths(matrix(5, 5)))  # should be 70


# since I was a little confused on whether or not the array was actually provided or not,
# I am going to use the array in this solution. For this solution, we will do some pruning
# by utilizing the integers within array to store data. Think of the sub problem as each
# element within the array will act as the top left of a sub matrix. So if we can
# store the number of paths from there to the bottom right, then we don't have to do
# that calculation again.
def calculate_paths2(arr):
    return

