
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
            if row + 1 < len(pyramid):
                pyramid[row+1][col] += (overflow * 1.0) / 2
            if row + 1 < len(pyramid) and col + 1 < len(pyramid):
                pyramid[row + 1][col +1] += (overflow * 1.0) / 2

    # query the row and glass
    return pyramid[query_row][query_glass] 

print(find_champagne_glass(2, 1, 1))
print(find_champagne_glass(5, 2, 1))