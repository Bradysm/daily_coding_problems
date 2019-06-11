# a wall consists of several rows of bricks of various integer lengths and uniform height
# your goal is to find a vertical line going from teh top to the bottom of teh wall that cuts
# through the fewest number of bricks. If the line goes through the edge between two bricks, this does
# not count as a cut

# given an input consisting of brick lengths for each row, return the fewest number of bricks that
# must be cut to create a vertical line

# so I guess I have a step ahead because this chapter in the daily coding problem is on hashtables,
# so I guess I have an understanding of what we need to use. Still, this can be a little tricky so
# bare with me

# Initially, I drew out the problem and tried to understand what we were focusing on. In this problem
# we aren't focusing on the bricks themselves, we're focusing on the ends of the bricks, or
# the vertical lines that they create after you place them. So in my head, I got rid of the bricks
# and decided to focus on the vertical lines that are created. In reality, we're trying to find
# the distance from the start that appears the most times when iterating through each row. I.e.
# the vertical line distance that appears the most when counting the distances in each row.
# If we can get this number, then we know the bricks that we have to cut through because those
# will be equal to # rows - (# rows containing most frequent line). Since we want to keep track of
# numbers and their frequencies, we can think of it as a key value pair, DING DING DING, dictionary time
# Now I choose to use something a little more 'fancy'. I chose to use a counter, since we are counting
# the number of times the vertical line shows up. This means I don't need to worry about checking
# for whether the key is in the counter, I can just add to it and wham, we get the number that we want.

# the last tricky thing that we need to look out for is that we need not count the vertical distance
# at the last brick. Since this will be the most counted line since the wall must end at this line.
# so you only need to iterate through the len(bricks[i])-2 (because -1 would include the last element)\

# once you've counted all of the vertical lines in each row, simply max over the values in
# the counter (or dictionary / hashmap) and then subtract this number from the number of
# rows in the wall, voila, you now have solved the problem!

from collections import Counter

count = Counter()  # this will be used to count the number of bricks ending at bick n

def cut_wall(bricks):
    for row in bricks:
        end = 0
        for brick in row[:-1]:  # include every brick but the last brick
            end += brick  # add the length of brick
            count[end] += 1  # increment the count of the brick that ends there
    return len(bricks) - max(count.values())  # subtract the bricks we don't cut through from the total rows


# test to make sure I'm not a dummy
b = [[3, 5, 1, 1],
     [2, 3, 3, 2],
     [5, 5],
     [4, 4, 2],
     [1, 3, 3, 3],
     [1, 1, 6, 1, 1]]

print(cut_wall(b))
