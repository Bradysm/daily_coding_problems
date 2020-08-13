"""
Hi, here's your problem today. (You've reached the end of the problems for now - in the meanwhile, 
here is a random question. And visit CoderPro for more practice!) This problem was recently asked by Google:

A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k, 
we want to figure out after k random moves by a knight, the probability that the knight will still be on the chessboard. Once the knight leaves the board it cannot move again and will be considered off the board.

Here's some starter code:

def is_knight_on_board(x, y, k, cache={}):
  # Fill this in.

print is_knight_on_board(0, 0, 1)


THOUGHT PROCESS:
Okay, so immediately when I read this question, I thought of a DFS that has to try all possible combinations of moves.
Since we need the probability that the night will land on the board given some completely random selection of moves
we need to first "experience" all of the moves and account for every possible scenerio that can happen. So, this
is essentially enumerating all move paths that are possible given k moves.

Now to first do this, we can think of this in a recursive nature (because for most this is easier to understand).
First we check to see if the current number move that we're on is greater than k (or if we decrement k, then we
check to see if it's equal to zero). If that is the case, we then check to see if we're on the board or not. We can then
return (1, 0) for 1 on board, zero off, or (0, 1) for 0 on the board and then 1 off. We can then build this solution up
and store the results in a cache, so if we cross paths with another path that has already found the solution for some
spot on the board, we can just utilize the already computed solution instead of redoing the work. This means that will
make at most O(8x8xk) calls or O(k).

We can then also write two helper functions to make the code easier to understand. One of the helper functions
will take the current coordinates of the chess piece and return true/false depending on whether the piece is on
the board or not. The second will take the current coordinates and return all of the possible positions that a night
can land based on the current location (8 different possibilities)

Continue scrolling for iterative solution
"""

def is_knight_on_board(x, y, k, cache={}):
    # call the recusive solution
    num_on, num_off = _knight_on_board_recursive((x,y), k, cache)
    return num_on / (num_off + num_on)

def _knight_on_board_recursive(pos, moves_left, cache):
    """
    Returns a touple (num_on, num_off) representing the number of 
    times the knight was on the board and the number of times
    the knight was off the board
    """
    # check to see if the current position is in the cache
    if cache.get(pos, None): return cache.get(pos)

    # check to see if we're out of moves
    if moves_left == 0: return (1, 0) if _on_board(pos) else (0, 1)

    # check to see if we're off the board
    if not _on_board(pos): return (0, 1)


    # otherwise, get the on off counters from the current position
    curr_on, curr_off = (0, 0)
    for new_pos in all_knight_moves(pos):
        on, off = _knight_on_board_recursive(new_pos, moves_left-1, cache)
        curr_off += off
        curr_on += on
    
    # add the probability to the cache and return it
    cache[pos] = (curr_on, curr_off)
    return cache.get(pos)


def all_knight_moves(pos) -> list:
    row, col = pos
    new_positions = []

    # upward moves
    new_positions.append((row-2, col+1))
    new_positions.append((row-2, col-1))

    # downward moves
    new_positions.append((row+2, col+1))
    new_positions.append((row+2, col-1))

    # rightward moves
    new_positions.append((row-1, col+2))
    new_positions.append((row+1, col+2))

    # lewftward moves
    new_positions.append((row-1, col-2))
    new_positions.append((row+1, col-2))

    return new_positions


def _on_board(pos) -> bool:
    """
    Checks to see if the current position is on
    an 8x8 board. We assume this will be the range
    from 0-7
    """
    row, col = pos
    if row not in range(0, 8): return False
    if col not in range(0, 8): return False

    return True




print(is_knight_on_board(0, 0, 1))


"""
Now that we've created a recursive solution. Let's recreate this in an iterative way.
I'm going to use the same functions that we created before, but this time instead
of using recursion, we will mimic it by utilizing a stack. This is essentially
what recursion is doing anyway. Each time a function gets called, it gets added to the
stack. We will just create that stack ourselves and remove the ability for us to 
create a stack overflow.
"""

def is_knight_on_board_iterative(x, y, k, cache={}):
    pos = (x, y)
    stack = [(pos, k)] # (curr_pos_knight, moves_left)

    landed_on = 0
    landed_off = 0

    while stack:
        curr_pos, moves_left = stack.pop()

        # check if the current position is in cache
        if moves_left == 0:
            landed_on += 1 if _on_board(curr_pos) else 0
            landed_off += 1 if not _on_board(curr_pos) else 0
            continue

        # not in cache, check to see if we're off the board
        if not _on_board(curr_pos):
            landed_off += 1
            continue

        # add all possible positions from our current position
        for new_pos in all_knight_moves(curr_pos):
            stack.append((new_pos, moves_left - 1))
        
    
    return landed_on / (landed_on + landed_off)


print(is_knight_on_board_iterative(0, 0, 1))