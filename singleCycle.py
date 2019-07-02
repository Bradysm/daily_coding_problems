# You are given an array of integers. Each integer represents a jump of its value in the array. 
# For instance, the integer 2 represents a jump of 2 indices forward in the array; the integer -3 represents a 
# jump of 3 indices backward in the array. If a jump spills past the array's bounds, it wraps over to the other side. 
# For instance, a jump of -1 at index 0 brings us to the last index in the array. 
# Similarly, a jump of 1 at the last index in the array brings us to index 0. 
# Write a function that returns a boolean representing whether the jumps in the array form a single cycle. 
# A single cycle occurs if, starting at any index in the array and following the jumps, 
# every element is visited exactly once before landing back on the starting index.

# Immediately when I see this problem, I see a directed graph with an adjacency list
# so each node (or element in the array) points to another node in the graph
# that you can move to, from the current node. So, to maneuver to the next index
# you take the index that you're at and whatever is at that index to it and that will take you
# to the next index that you can go to. welll..... I wish that was all it was for this problem.
# you also need to account for the index going out of bounds, and you need to account for negative
# numbers. Rolling around the array is easy, so we will just use mod len(array) to do this (just like a circular queue)
# you will then also need to add the length of the array, to take care of negative value roll over. Few, okay
# now we can move around correctly. So how do we detect a cycle with all of the nodes?

# so by this definiton, if we start anywhere in the graph, we should land back at that node
# and only visit the nodes in the graph exactly once. So don't get tricked with this problem
# and try running this algo for each node in the graph. You only need to prove it for one
# and it inductively proves the rest. So, for this problem, well start at the zero index
# and then hopefully land back in the zeroth index.

# what happens if there is a cycle that doens't land back at zero? This means that we
# need to keep track if nodes within the graph have already been visited. To do this
# I utilize the graph given and set that nodes next value to None. This means we've already
# been there at that node. Lasltly, how do we know when to stop? We stop when the next value
# is none (or already visited) or if the next value is zero and zero has already been visited
# This will allow us to differentiate between a cycle and a single cycle

# To decide what to return, we check to see that all nodes in the graph are visited
# and if the nextNode is zero. If either of these are not true, return False, otherwise True

# O(n) time and O(1) space

def hasSingleCycle(array):
    nxtNode = 0 # start at the zero index
    while nxtNode is not None:
		if nxtNode == 0 and array[0] == None: break # made it back to start
		temp = array[nxtNode]
		array[nxtNode] = None # mark as visited
		nxtNode = (nxtNode + temp + len(array)) % len(array) if temp is not None else None
	
	# check to make sure all visited and nxtNode is 0
    return False if any(array) or not nxtNode == 0 else True