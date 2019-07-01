# Here comes another graph problem!!!! WOOT WOOT MY FAVVVVVV

# given a NxM matrix containing 1's and 0's (0's representing land, and 1's representing water)
# return an array containing the sizes of rivers within the map
# A river consists of 1's that are adjacent to eachother (up, down, left, and right)

# what we want to do is simply utilize the techniques that we've done in the cloud and island
# problem. This will be running DFS on each graph node (this is simply and element in the matrix)
# and then counting it as an object we need or not, and then updating the node as visited
# When I initially wrote this algo, I had the visited too late and the recursive stack overflowed
# Make sure that when you're doing a graph problem, that when you initally touch a node, you
# mark it as visited or else you can easily run into problems where you loop forever because
# the node believes it's not visited. We're going to use a sneaky trick to mark it as visited
# by setting the graph index to -1. We will do this just for the water in this problem,
# but you can do it for anything on the graph it doesn't really matter. Okay, so when
# we get to a piece of water, we then want to call DFS on that graph node. We can then
# move forward from there and keep calling that in all directions until we've touched all
# connecting water. Whenever we touch a piece of water, we will add one to the water count
# This value will then be retuned by DFS and added to the river sizes array. Voila. Fun graph problem


# [[1 0 1 0]
#  [1 1 1 0]
#  [1 0 0 1]
#  [0 1 0 0]
#  [0 1 0 0]]

# this should return [6, 2, 1]

def dfs(land, row, col):
    inRange = row in range(len(land)) and col in range(len(land[0]))
    if not inRange: return 0 # went out of range
    # get the topology and mark as visited
    topology = land[row][col]
    water = 0
    if topology == 1: # check to see if we're at water
        land[row][col] = -1
        water += 1 # we're on water, add one
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # explore graph in each direction
            water += dfs(land, row+dr, col+dc)
    return water

def river_size(land):
    rivers = [] # array used to create the rivers
    for row in range(len(land)):
        for col in range(len(land[0])):
            if land[row][col] == 1: # check to see if we're on water
                river_size = dfs(land, row, col)
                rivers.append(river_size)
    return rivers

lmap = [[1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 0]]

print(river_size(lmap))