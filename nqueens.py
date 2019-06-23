# The way I was going to initially solve this problem was with the AC-3
# algorithm. Because each column represents a state of possible
# variables that can be assigned, and then as you place
# the values, you eliminate the values from the tail arc. I know that probably
# wasn't the easiest description to follow, but I hope that you can look into
# AC-3 and understand what I am talking about. The reason why this isn't
# going to work is because it finds ONE solution if there is one
# think of k-coloring, all we want is one coloring of the states. It doesn't
# matter how we get there, or if there is other colorings, we just care about 1
# since this problem cares about all queen representations on the board,
# we can't use AC-3

# okay back to the drawing board. Let's assign a queen to each column
# and determine queens by their column. Then we can "place" a queen on the board
# by going to their column (or index in the board array) and then changing that
# element to the row that we're placing the queen in. We then move onto the
# next column and try to place a queen at all the rows that are valid.
# we continue doing that until the column we're at is one past the end
# of the board, and when we get there, we know that board position
# is valid because for every k column, assuming the board is valid up to that
# point, we then place a valid position and move to the k+1 column. Thus
# it acts in an inductive way so we know the board is valid from valid decisions
# from each column. The runtime is O(n^n)
# this is not great at all haha

def n_queens(n):
    p = [-1 for i in range(n)]
    return eq_help(0, p, n)

def valid(col, row, qplacements):
    """
    Checks to see if the current queen placement is valid
    :param col: column of that specific queen
    :param row: row the queen is being placed in
    :param qplacements: current placements of queens
    :return:
    """
    # need to just validate to the right and diagonals
    # the positions will be an array where each index represents the
    # queens column, and the
    for c, r in enumerate(qplacements):
        if r == -1: continue  # no queen placed yet
        if r == row: return False  # placed in the same row
        if abs(c-col) == abs(r-row): return False  # in the diagonal
    # return true otherwise
    return True


def eq_help(qcol, queens, n):
    if qcol == n:
        print(queens)  # valid board
        return
    for row in range(n):
        if valid(qcol, row, queens):
            queens[qcol] = row  # place the queen at the row
            eq_help(qcol+1, queens, n)  # place the q+1 queen
            queens[qcol] = -1  # take off board


print('print all the ways to place 4 queens')
n_queens(4)

print('\nprint all the ways to print 5 queens')
n_queens(5)