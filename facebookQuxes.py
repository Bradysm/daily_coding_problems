"""
 Good morning! Here's your coding interview problem for today.
 This problem was asked by Facebook.
 On a mysterious island there are creatures known as Quxes which come in three colors: 
 red, green, and blue. One power of the Qux is that if two of them are standing next to each other, 
 they can transform into a single creature of the third color.

 Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

 This looks like a classic recursion problem to me. You need to try all of the different combinations if possible
 to be able to determine the min number of possible qux on the island. To do this, we will choose to either pair
 them or we will not pair them. But we can only pair them if they're not next to someone of the same color as them
 We then keep moving down with a swap index, and return the size of the array at the end. We can then take the min 
 as we go back up the recursion tree to then get the minimum number possible.

 It is important to note that a transformation, you need to go one back becuase this could potentially cause
 the index before to now swap with the newly transformed, so you can see that I take the max of 0 and i-1
 to ensure that we never create a negative index
"""


def determineMinimumQux(quxes: list) -> int:
    return recusiveSwaps(0, quxes)

def recusiveSwaps(i: int, arr: list) -> int:
    # check to see if swap index is greater or equal to arr length
    if i >= len(arr): return len(arr)

    # choice of not transforming
    minQuxes = recusiveSwaps(i+1, arr)

    # Choice of transforming (must be a valid transform)
    if validTransformationIndex(i, arr):
        transformmedColor = transform(arr[i], arr[i+1])
        newArr = arr[:i] + [transformmedColor] + arr[i+2:]
        minQuxes = min(minQuxes, recusiveSwaps(max(i-1, 0), newArr))

    return minQuxes



def validTransformationIndex(i, arr):
    hasNext = (i+1) < len(arr)
    return hasNext and (arr[i] is not arr[i+1])


def transform(color1, color2) -> str:
    colorSet = set([color1, color2])
    if colorSet == set(["R", "B"]): return "G"
    if colorSet == set(["R", "G"]): return "B"
    return "R"



# can only turn into two
testQuxesTwo = ['R', 'B', 'G']

# should be 1
testQuxes = ['R', 'G', 'B', 'G', 'B']

print(determineMinimumQux(testQuxes))
print(determineMinimumQux(testQuxesTwo))