def levenshteinDistance(str1, str2):
	if str1 == "" and str2 == "": return 0 # we made it to the bottom
	if str1 == "": return len(str2) # string 1 is empty
	if str2 == "": return len(str1) # string 2 is empty
	
	if str1[-1] == str2[-1]:
		return levenshteinDistance(str1[:-1], str2[:-1])
	
	remove = 1 + levenshteinDistance(str1[:-1], str2)
	insert = 1 + levenshteinDistance(str1, str2[:-1])
	sub = 1 + levenshteinDistance(str1[:-1], str2[:-1])
	return min(remove, min(sub, insert))




import sys
def edit_distance(str1, str2):
    if str1 == "" and str2 == "": return 0 # we made it to the bottom
    if str1 == "": return len(str2) # string 1 is empty
    if str2 == "": return len(str1) # string 2 is empty

    # create the table to be used, 0 index will be empty subtring
    table = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)] 
    
    for str1_i in range(len(table)): # iterate through the string1 characters
        for str2_i in range(len(table[0])): # iterate through the string2 characters
            if str1_i == 0 and str2_i == 0: continue
            # get the characters and check for equality
            same = sys.maxsize # set it to the max size
            if str1_i > 0 and str2_i > 0:
                # get the two characters
                c1 = str1[str1_i-1]
                c2 = str2[str2_i-1]
                if c1 == c2: same = table[str1_i-1][str1_i-1]
             
            remove = sys.maxsize if str1_i - 1 < 0 else table[str1_i-1][str2_i]
            insert = sys.maxsize if str2_i - 1 < 0 else table[str1_i][str2_i-1]
            replace = sys.maxsize if str1_i - 1 < 0 or str1_i - 1 < 0 else table[str1_i-1][str2_i-1]
            # find the min move and add one to it
            min_move = min(remove, min(insert, min(replace, same)))
            table[str1_i][str2_i] = min_move + 1
            print("str1_i: {x} str2_i: {y} distance {dist}".format(x=str1_i, y=str2_i, dist=table[str1_i][str2_i]))
    
    return table[len(table)-1][len(table[0])-1]

print(edit_distance("y", "ay"))