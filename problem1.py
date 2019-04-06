#Good morning! Here's your coding interview problem for today.

#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?

nums = [10, 100, 4, 6, 7, 81, 2, 5, 8, 1, 0, 66, 78]
nullList = [] # check on an empty list
oneList = [1] # check on a list with one element


def sum_to_k(nums, k):
    """nums - this is a list contianing numbers
       k - number seeing if we can sum to
    """
    visited = set()  # set that we will use to store seen values
    # check to see if it's in the set, add num if not valid yet
    for num in nums:
        if k-num in visited: return True
        else: visited.add(num)
    return False  # there isn't a numbers containing the sum


# test to make sure that it's working
print "Valid: ", sum_to_k(nums, 11)
print "Valid: ", sum_to_k(nums, 1)
print "Invalid: ", sum_to_k(nums, -1)
print "Empty: ", sum_to_k(nullList, 0)
print "One num should be false: ", sum_to_k(oneList, 1)
