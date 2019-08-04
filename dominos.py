# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given a string with the initial condition of dominoes, where:

# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side

# Figure out the final position of the dominoes. 
# If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

# Example:
# Input:  ..R...L..R.
# Output: ..RR.LL..RR

# Okay so I remember trying to do this problem around a year ago when my interview journey began
# I was on leet code, saw this problem, and thought that it couldn't be too bad, so I sat there an tried to figure
# it out but I continually failed. My problem was that I didn't understand how to handle the actions and 
# organize them in a way that it took into account "time". You will see how I do this wiht my solution

# when you initially see this problem, you think that you can go left ot right and then change the values
# as you move down, but this is wrong. The reason being is that if you go left from right, you assume
# that the "time" passing first goes from left to right and that the actions don't happen in steps that 
# sequentially go together. So, how can we mock this time step?

# the way that you can mock time moving is by using a QUEUE. This will allow you to mimic "passes of time" over
# the array and allow you to take into account the time that things happen. So, when you change an index, you will
# then put that domino that you just changed at the BACK of the queue, so everything infront of it still
# will happen first before that domino is processed.

# we can then create the initial time step by taking one pass over the inital string and filling it with
# the indexes that contain actions. Once we have these indexes, we will process them and then process
# the coressponding domino that needs to be updated. Once we update that new index, we will place that
# new index at the back of the queue to ensure that every action that needs to be processed in the time
# step before it, does get processed.

# we then continue this iteration until thq queue is empty.
# this will give us O(n) time and space because we create the queue and in the worst case will have to update
# every index of the dominos

# remember, this stuff is not easy. Don't get discouraged if you can't solve the problem or if you
# don't get it in the same time complexity. It takes a while to get good at interviewing and I'm not at
# the "master" level that I want to be at either. Just take it one day at a time and one problem at a time


def push_dominos(dominos):
    res_dominos = [domino for domino in dominos]
    queue = [i for i, domino in enumerate(dominos) if not domino == '.']

    while len(queue) > 0: # iterate over the changes
        action_i = queue.pop(0)
        if res_dominos[action_i] == 'R': # check to see if falling right
            attemptPushRight(action_i, res_dominos, queue)    
        if res_dominos[action_i] == 'L':
            attemptPushLeft(action_i, res_dominos, queue)
    return ''.join(res_dominos)

def attemptPushRight(action_i, res_dominos, queue):
    update_i = action_i + 1
    # check to make sure the updated index is within bounds and next is not falling left
    if update_i < len(res_dominos) and res_dominos[update_i] is '.': # check to make sure unvisited
        if (update_i+1 == len(res_dominos) or res_dominos[update_i+1] is not 'L'):
            res_dominos[update_i] = 'R' # update to falling right
            queue.append(update_i)

def attemptPushLeft(action_i, res_dominos, queue):
    update_i = action_i - 1
    if update_i > -1 and res_dominos[update_i] is '.':
        if (update_i-1 < 0  or res_dominos[update_i-1] is not 'R'):
            res_dominos[update_i] = 'L' # update to falling right
            queue.append(update_i)

test = '..R...L..R.'
test2 = '.R...LRR...L'
print(push_dominos(test))
print(push_dominos(test2))
