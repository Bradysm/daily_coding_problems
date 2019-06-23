# Implement the "paint fill" function that one might see on many image editing programs.
# Thatis, given a screen (represented by a 2d array of colors), a point, and a new color,
# fill in teh surrounding area until the colro changed from the original color

# okay, well, immediately I am thinking of graph theory when I see this problem
# the reason being is that the section of color that we're changing acts like a graph
# by this I mean that only the color that is connected through up, right, left and down
# movements should be the color that is changed. If we see the color anywhere else
# on the screen, we shouldn't change it because it is not part of the "fill area"
# that we're supposed to be updating. So, we should think of the inital point
# as the starting point in the graph. We then want to expand out from the starting
# point using a DFS (you can also use BFS, but you will have to handle it a bit differently)
# When you expand from teh points, if the new "graph node" contains the color that
# you need to change, you change the color and then expand from that node because
# there could be more pixels that you need to change which are connected to that one

# where does the base case happen? The base case will happen when the color
# at the cell is not the color we're trying to change, or if we're outside of the display

def paint_fill(display, point, color):
    """
    Updates the display and fills the surrounding area of that point
    from the original color to the new one
    :param display: 2D array of colors
    :param point: (row, col) tuple
    :param color: character
    """
    if display is None or len(display) == 0: return # invalid display
    og_color = display[point[0]][point[1]]  # get's the OG color
    pf_help(display, point, color, og_color)
    return display


def pf_help(disp, pt, newc, ogc):
    """
    fills in the display with the new color using graph theory
    :param disp: 2D matrix
    :param pt: current point on the display
    :param newc: new color to change to
    :param ogc: original color
    """
    row, col = pt
    if row not in range(len(disp)) or col not in range(len(disp[0])): return  # invalid point
    if not disp[row][col] == ogc: return  # not a color that we need to change
    disp[row][col] = newc  # change the color
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        pf_help(disp, (row+dr, col+dc), newc, ogc)


# testing display
d = [['W', 'W', 'W', 'B', 'B', 'Y'],
     ['Y', 'Y', 'Y', 'Y', 'B', 'Y'],
     ['W', 'W', 'Y', 'Y', 'Y', 'Y'],
     ['G', 'B', 'G', 'Y', 'Y', 'B'],
     ['G', 'B', 'R', 'G', 'Y', 'B'],
     ['G', 'B', 'B', 'G', 'Y', 'B']]

# fill the space with oragane
d = paint_fill(d, (3, 3), 'O')

# reprint the value
for r in d:
    print(r)

