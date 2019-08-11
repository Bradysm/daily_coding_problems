# Hi, here's your problem today. This problem was recently asked by Amazon:

# You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

# Example:

# grid = [[1,  2,  3,  4,  5],
#        [6,  7,  8,  9,  10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20]]

# The clockwise spiral traversal of this array is:

# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

# to me, this problem is less hard, and more just implementation.
# It's not really challenging to create 4 for loops and iterate through the matrix
# it's mainly just finding how to end and where to start the various traversals
# Once you understand that you create the four bounds for iteration (these bounds encapsulate the permieter of
# a rectangle that you're iterating over) then you can easily come up with the solution. One thing
# that you can see was a bit tedious was decrementing the nuber of nodes. This is because ints are passed
# by copy so you can't simply just pass it to the function and have it change (unless you encapsulate it in
# an array or something). Either way, I'm sure you can find some convergence to test to make sure 
# that you want to keep going or not by seeing if the corners of the square are valid, but I chose to
# do it this way for the sake of time. Make sure you understand why I added the checks to see if there are still nodes to 
# visit when I call the methods. Notice that if I didn't do that, then up would produce 8 again for the second
# matrix. Very interesting huh? So this problem may not be so easy after all? I still don't think it's too
# bad and half way through doing this comment I changed the ndoes to visit to an array so I could
# pass it by reference. Cheers. Thanks Amazon for trying to trick me!

def spiral_print(nums):
    if not nums or nums is None: return # get rid of bad matrix's
    start_row = left_col = 0 # this will be the starting
    right_col = len(nums[0]) - 1
    end_row = len(nums) - 1 
    nodes_to_visit = [len(nums) * len(nums[0])]

    # continue going as long as there are nodes to visit
    while nodes_to_visit[0] > 0:
        visit_right(nums, start_row, left_col, right_col, nodes_to_visit)
        visit_down(nums, right_col, start_row + 1, end_row, nodes_to_visit)
        visit_left(nums, end_row, right_col-1, left_col, nodes_to_visit)
        visit_up(nums, left_col, end_row-1, start_row+1, nodes_to_visit)

        # update start end left and right (converge them towards the center)
        start_row += 1
        end_row -=1 
        left_col += 1
        right_col -= 1


def visit_right(matrix, fixed_row, start_col, end_col, nodes_to_visit):
    if not nodes_to_visit[0]: return
    for col in range(start_col, end_col+1):
        print(matrix[fixed_row][col])
        nodes_to_visit[0] -= 1

def visit_down(matrix, fixed_col, start_row, end_row, nodes_to_visit):
    if not nodes_to_visit[0]: return
    for row in range(start_row, end_row+1):
        print(matrix[row][fixed_col])
        nodes_to_visit[0] -= 1

def visit_left(matrix, fixed_row, start_col, end_col, nodes_to_visit):
    if not nodes_to_visit[0]: return
    for col in range(start_col, end_col-1, -1): # we need to include the end so we minus one and incrementer is in reverse
        print(matrix[fixed_row][col])
        nodes_to_visit[0] -= 1

def visit_up(matrix, fixed_col, start_row, end_row, nodes_to_visit):
    if not nodes_to_visit[0]: return
    for row in range(start_row, end_row-1, -1): # we're going up so we subtract
        print(matrix[row][fixed_col])
        nodes_to_visit[0] -= 1



test_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15], 
    [16, 17, 18, 19, 20]]

test_matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

print('\ntesting on matrix 1')
spiral_print(test_matrix)

print('\ntesting on matrix 2')
spiral_print(test_matrix2)