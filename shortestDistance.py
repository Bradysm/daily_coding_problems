# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board.
# Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate,
# return the minimum number of steps required to reach the end coordinate from the start.
# If there is no possible path, then return null. You can move up, left, down, and right.
# You cannot move through walls. You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
#and start = (3, 0) (bottom left) and end = (0, 0) (top left),
# the minimum number of steps required to reach the end is 7,
# since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

"""
For this problem, it's important that you immediately think of algorithms that involve the shortest
path to get to some place. Things like A* and Djikstras algo should pop into your head. For me,
it makes more since to think of each element wihtin the matrix as a node within a graph.
Each node connects to its neighbors, (up, left, down, right)

Let's first think of some of the complexities of the problem (or lack thereof). First things first,
we don't actually care about the path, we just care about the length traveled. Second, every distance
traveled is a length of 1, and since we know the start and end goal, we could use a heuristic of manhattan
distance to allow us to use A* algorithm. Lastly, we need to know about the children that can be added
as the next step from every step that we're currently at. If a neighbor is a True flag, then we don't
want to add it to the priority queue because it represents a wall. We can only add up down left and right
so we need to check the boundries of the walls
"""
import heapq

def manhattan_distance(start, end):
    """
    calculates the manhattan distance between two points
    :param start: tuple containing start coordinates (row, col)
    :param end: tuple containing end coordinates (row, col)
    :return: taxi distance between two points
    """
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def neighbors(state, map):
    """
    returns a list of neigh
    :param state: current state within the algo
    :param map: map containing true and false values
    :return: list containing tuples with neighbors
    """
    neighbors = []
    if state[0] + 1 < len(map) and map[state[0]+1][state[1]] is not True: # moving down
        neighbors.append((state[0]+1, state[1]))
    if state[0] - 1 > -1 and map[state[0]-1][state[1]] is not True: # moving up
        neighbors.append((state[0]-1, state[1]))
    if state[1] + 1 < len(map[0]) and map[state[0]][state[1] + 1] is not True: # moving right
        neighbors.append((state[0], state[1] + 1))
    if state[1] - 1 > -1 and map[state[0]][state[1] - 1] is not True:
        neighbors.append((state[0], state[1] - 1))

    # return the neighbors from the state
    return neighbors

def is_goal(state, goal):
    if state[0] == goal[0] and state[1] == goal[1]:
        return True
    return False


def shortest_distance(map, start, goal):
    """
    Given a map (matrix) of true and false booleans
    return the shortest distance between two spots
    :param map: matrix containing list
    :param start: tuple containing start coordinates (row, col)
    :param goal: tuple containing end coordinates (row, col)
    :return:
    """
    # priority queue used to implement A*
    p_queue = [(0, ([], start))]  # (f, (path, state))
    visited = set()  # set containing the visited nodes

    while len(p_queue) > 0:
        # pop off most optimistic node, add to visited
        path, state = heapq.heappop(p_queue)[1]
        visited.add(state)
        # check if it's the goal state
        if is_goal(state, goal):
            return len(path)
        # add children if not
        for node in neighbors(state, map):
            if node not in visited:
                new_path = path + [node]  # create a new path object
                heuristic = manhattan_distance(goal, node)  # find manhattan heuristic
                heapq.heappush(p_queue, (heuristic + len(new_path), (new_path, node)))

    # there is no path from start to goal
    return -1


# testing for map distance
t_map = [[False, False, False, False],
         [True, True, False, True],
         [False, False, False, False],
         [False, False, False, False]]

print shortest_distance(t_map, (3, 0), (0, 0))
print shortest_distance(t_map, (0, 3), (3, 3))
