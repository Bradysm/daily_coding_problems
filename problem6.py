# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

# The key to this problem is to understand that for each number, we can either count
# just the singular number, or we can check to see if that number and the next one
# add up to <= 26 and then move the count by an increment of 2. The best way for me
# to think about this was looking at the problem from a tree standpoint. If you think
# of the problem as counting from each index, than we can do some pruning to the
# tree by using dynamic programming by storing intermediate values

# ex) for the string '111', we can think of the tree as storing the index of the current
# character that we will be looking at for counting. So from the first index, we can either
# go to index 1, or we can go to index 2 (going to index 1 means we only read the first 1,
# and going to index 2 means that we read the first 2, and their int representation was
# <= 26 so it's a valid path). We can continue doing this splitting until we get to
# an index that is equal to the length of the string, once we get here we return 1 because
# this represents 1 path that we could count. we then backtrack up and continue on with the
# next path. To make the algo more time efficient, we can use an array to keep track
# of the calculated counts from an index. Thus, once we reach that index again, we no longer
# have to recalculate all of the possibilities
#
#   `        0
#         1     2
#       2  3      3
#      3
#
#

def decode(str):
    """takes an encodes string returns the number of ways to decode it
       str: str"""
    return decode_help(str, [-1] * len(str), 0)


def decode_help(msg, arr, i):
    """This function will decode a str given the string of numbers
        arr will be used for dynamic programming so we don't have to calculate
        values from the same index multiple times
        msg: str - contains the encoded message
        arr: list - list of calculated values
        i: int - integer representing the index of the string we're at"""
    if i == len(msg): return 1  # this is one way to count
    if arr[i] is not -1: return arr[i]  # we've already calculated the value

    # count the number of ways from i
    count_i = 0
    count_i += decode_help(msg, arr, i + 1)
    if i+1 < len(msg) and int(msg[i:i+2]) <= 26:
        count_i += decode_help(msg, arr, i+2)

    # update the array and return the number of counts
    arr[i] = count_i
    return arr[i]


# run tests on the program
msg1 = '111'
msg2 = '11234'
msg3 = '27'
msg4 = ''
print (decode(msg1))
print (decode(msg2))
print (decode(msg3))
print (decode(msg4)) # there is only one way to decode an empty message
