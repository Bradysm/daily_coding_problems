# You're given three inputs, all of which are instances of a class that have an "ancestor" property pointing to their youngest ancestor. 
# The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor), 
# and the other two inputs are descendants in the ancestral tree. 
# Write a function that returns the youngest common ancestor to the two descendants.

# initially when I saw this problem, I got really excited, because I love working with trees and graphs
# Whenever you tackle a tree or graph problem, I highly recommend you write it out and try working through
# it on a piece of paper or a whiteboard. That will really help you come up with an algorithm!

# Try 1: in the first 30 seconds I came up witha  solution that involved storing the path of one
# of the persons trail to the top ancestor, using a set (youll see why soon). Then traversing
# up the tree again with the second person until that person up the path is seen in the set.
# we use a set to allow for O(1) lookup

# this will take O(d) space and time. The d being the deeepest depth of the tree

# Try 2: Can we do this problem without extra space?
# yes, and the best way for me to think of this problem was like another problem that I saw
# where you have to find the first intersecting node in the LL
# for that problem you find the length of both LL's move the pointer pointing to the head
# of the longest list down until the current pointer points to a node at the same length
# as the shorter list (you with me still?) Then, you increment the two pointers down
# the list until they are both pointing to the same node. This is the same thing for this problem.
# we find the depth for both of the people, then increment up the tree for the deeper node. Once
# they are on the same level, we increment them up one each time until they point to the same node.
# this will always converge because they must converge to the top most ancestor node. Because
# working up the tree decreases the path options instead of increasing them

# O(d) time and O(1) space!! Viola!




def getDepth(person):
    depth = 0
	currAncestor = person
	while currAncestor is not None:
		depth += 1
		currAncestor = currAncestor.ancestor
	return depth


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOfDescOne = getDepth(descendantOne) # get the depths
	depthOfDescTwo = getDepth(descendantTwo)
	
	# get nodes on the same level
	while depthOfDescOne > depthOfDescTwo:
		depthOfDescOne -= 1
		descendantOne = descendantOne.ancestor
	
	while depthOfDescTwo > depthOfDescOne:
		depthOfDescTwo -= 1
		descendantTwo = descendantTwo.ancestor 
	
	# increment up tree, until point at same node
	while descendantOne is not descendantTwo:
		descendantTwo = descendantTwo.ancestor 
		descendantOne = descendantOne.ancestor
	
    return descendantTwo