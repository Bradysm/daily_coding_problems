# this problem has been asked by interviewers like google, fb, etc
# implement an algorith to PRINT ALL VALID (eg properly opened adn closed) combinations
# of n pair of parentheses


# Since the problem initially said that we want to print ALL of the combinations
# I immediately thought of writing a recursive algorithm. Although this may not
# be correct at first, it was the decision that I decided to make and it helps
# to tell your interviewer why you have this intuition. Anyways, on with the problem.

# Since I have had to implement a compiler checker a million times for interviews
# to check to see if the parentheses were closed or opened, I had some intuition
# on how to solve this problem, but nothing too great.

# after taking a greater look at the problem, a few things stuck out to me.
# 1. you always need to start with an open parentheses
# 2. you need to keep track of the number of pairs of parentheses within your string
# 3. you should know the number of "open" sets within the curret string that you're building
# when I say an "open" set, I mean that there is an open bracket that still needs to be closed

# after looking over these numbers, I realized that there is a connection between theses integers
# and the brackets. For every open bracket to the string, we can add one to the total number
# of open pairs within our current string, but it will not affect the number of closed pairs
# because we haven't closed anything by adding it. WHen you add a closed bracket to the 
# string, you decrement the number of open paren and the number of pairs left. This is because
# a closing bracket will close the open bracket and it will complete a pair that we want.

# we then need to look at the base cases for these numbers.
# The easiest one is to know that if the open value becomes negative
# then we've closed a parentheses that does not have an open one to pair with, thus making an invalid string
# The second case is that the number of open brackets exceeds the number of pairs that are still
# left to be made. We can check for these at the beginning of the recursive call and backtrack
# when we reach these invalid states. Lastly, we know it's a valid string
# when the number of pairs is zero and open parentheses is zero.
# Although the case where pairs is zero and opn isn't zero isn't really possible, I like adding the check
# just for safety. This will have O(2^n) time complexity

# lastly, we're guarunteed to have all unique solutions because at each step in the recursive
# solution, a decision is made for the specific index within the string. Since that decision
# cannot be made again, we are guarunteed to have unique solutions

# To save some memory and time complexity of creating a new string, 
# each time you append, I'm using a list and then concatinating the string together at the end.

def paren(n):
    # call the helper function
    paren_help(0, n, [])


def paren_help(opn, pairs, brackets):
    # check if we've added too many openings or too many closings
    if opn < 0 or opn > pairs: return 
    if pairs == 0 and opn == 0: # check to see if valid string
        print("".join(brackets)) 
        return # move back
    
    # try to add bracket, move in the direction and then backtrack
    for paren, diffo, diffp in [("(", 1, 0), (")", -1, -1)]:
        brackets.append(paren)
        paren_help(opn + diffo, pairs + diffp, brackets)
        brackets.pop()
    

# testing to make sure it works
print('Set of 5')
paren(5)

print('\nSet of 4')
paren(4)