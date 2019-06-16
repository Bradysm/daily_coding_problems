# Imagine a robot sitting on the upper left corner of the grid with r rows
# and c columns. The robot can only move in two directions, right and down, but certain cells are "offliits"
# such that the robot cannot step on them. Design an algo to find A PATH for the robot from the top left 
# to the bottom right.


# first things first, the problem specifies that we need to only find one path
# it also never specifies if it has to be the optimal path or not, so I'm going to
# assume that we can just use DFS and call it a day
# for this problem, I'm going to be using a build up "DP" style of code that
# will focus on building the solution from the bottom up.
# What this will do is continue calling the function until we get to the 
# final destination. Once we get there, it will return an empty list, and
# then we will build the list back up by adding the move that was taken
# and then returning the list. 
# 
# Since this did come from the recursive section of CCI, I decided to go with
# the recrusive DP implementation, but I would normally use a stack and use backtracking
# to generate the path. Just so you can save some time and space complexity.

# also, quick note. Since we are returning the list to the stack frames, we don't allocate
# the space on the frame to store it as a parameter. A top down solution would require this
# and it would take up more space. This is something that you could talk to your interviewer about


from grid import matrix

def robot_path(grid):
    """
    function to generate robot paths 
    """
    return rpath_help((0,0), grid)

def rpath_help(pos, grid):
    """
    Helper function used to generate the path
    """
    if pos[0] >= len(grid) or pos[1] >= len(grid[0]) or grid[pos[0]][pos[1]] == -1:
        return None # we went off the grid, or invalid space
    if pos[0] == len(grid) - 1 and pos[1] == len(grid[0]) -1: 
        return [] # return an empty path
    
    # build the path from the bottom up
    for dr, dc in [(1, 0), (0, 1)]:
        npos = (pos[0] + dr, pos[1] + dc) # create the new pos
        path = rpath_help(npos, grid)
        if path is not None:
            path.insert(0, (dr, dc)) # append the move onto the path
            return path
    # if we didn't find a valid path, return None
    return None
    

# testing
m = matrix(5, 5)
print(robot_path(m))
