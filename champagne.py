# consider a pyramid of champagne glasses where the the 1st row has 1 glass
# the second row has two glasses, the third row has three, and so on.
# we pour a certain amount of champagne into the top glass, and that glass
# fills and pours equally into the left and right glasses of that glass.
# Note that if 2 glasses are poured into one glass, 0.5 of a glass will fall to the left
# and 0.5 will fall to the right.

# given a row for the glass, and the glass number in that row, return the 
# amount of champagne that is in that glass
# assume that if we're at the bottom row it still spills over 
# note that the values given are 0 indexed. So the zero'th row will have 1 glass

# so when I saw this problem, I realized that we want to overflwo to the row
# below us and the row below us and the column to the left. The reason I saw
# this is I started drawing out a tree, and drew the arrow that created the pour
# direction. If we follow the arrows, we see that the (row-1, col) pours into 
# the glass at (row, col) and the (row-1, col-1) pour into that glass as well
# I then thought of building the solution with a matrix and going row by row
# all the way through the row that we're searchig for.; We then return the 
# value at the matrix location query_row, query_col. This is like a DP
# build up problem. Very nice, O(n^2) time and O(n^2) space


# query_row is the row that the glass is in
# query_glass is the col that the glass is in

def find_champagne_glass(poured, query_row, query_glass):
    pyramid = [[0 for _ in range(i+1) ] for i in range(query_row+1)] # create a "pyramid" matrix, because the row determines it
    pyramid[0][0] = poured
    # build pyramid down until row, col
    for row in range(len(pyramid)):
        for col in range(row + 1):
            # subtract one cup and move overflow to the left and right cups
            overflow =  pyramid[row][col]-1 if pyramid[row][col]-1 > 0 else 0
            pyramid[row][col] -= overflow # update to the correct amount left in glass
            if row + 1 < len(pyramid):
                pyramid[row+1][col] += (overflow * 1.0) / 2
            if row + 1 < len(pyramid) and col + 1 < len(pyramid):
                pyramid[row + 1][col +1] += (overflow * 1.0) / 2

    # query the row and glass
    return pyramid[query_row][query_glass] 

# testing
print(find_champagne_glass(2, 1, 1))
print(find_champagne_glass(5, 2, 1))
print(find_champagne_glass(10, 1, 1))