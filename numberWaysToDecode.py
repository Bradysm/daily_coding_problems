
"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def find_number_of_ways_to_decode(s) -> int:
    # base cases
    if len(s) == 0: return 0
    if len(s) == 1: return 1
    if len(s) == 2: return 2

    # take the first number off and find the ways to get the rest
    total_ways = find_number_of_ways_to_decode(s[1:])

    # check to see if we can take two
    total_ways += 0 if int(s[:2]) > 26 else find_number_of_ways_to_decode(s[2:])

    return total_ways


def find_num_ways_decode_iterative(s) -> int:
    # if s empty return 0
    if not s: return 0
    if len(s) == 1: return 1

    # create an array of zeros, storing the computed values so we can build the solution
    ways_decode = [0 for i in s]

    # base cases
    ways_decode[-1] = 1
    ways_decode[-2] = 2

    # move from the back to the front
    for i in reversed(range(len(s)-2)):
        ways_decode[i] += ways_decode[i+1]

        # check to see if we can split it at 2
        ways_decode[i] += 0 if ((i+2) >= len(s)) or int(s[i:i+2]) > 26 else (ways_decode[i+2])

    return ways_decode[0]

    
print('Recursive', find_number_of_ways_to_decode('11111'))
print('Iterative', find_num_ways_decode_iterative('11111'))


print('Recursive', find_number_of_ways_to_decode('111112'))
print('Iterative', find_num_ways_decode_iterative('111112'))


print('Recursive', find_number_of_ways_to_decode('1115112'))
print('Iterative', find_num_ways_decode_iterative('1115112'))