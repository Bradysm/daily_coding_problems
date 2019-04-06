# given a list of numbers (in sorted order) determine the number that is missing from the list
# only one number will be missing and the range of the numebrs will be filled besides that
# numbers will go from 1-100
numbers = [x+1 for x in range(100)] # creates a list of 1-100
missing3 = [x for x in numbers if not x == 3] # missing 3
missing59 = [x for x in numbers if not x == 59] # missing 59
missing100 = [x for x in numbers if not x == 100]
missing1 = [x for x in numbers if not x == 1]

def detect_missing_num(nums):
    """given a list of numbers, return the number that is missing from the list
       nums - list of numbers with range from 1-100, missing one number


       Goal: brute for solution is to run through the indexe one by one and
        check to see when index+1 does not equal the current number
        O(n)

        A faster solution is to treat it like a binary search and
        split the numbers in half. If the current index+1 equals the
        number at that index, then we know everything to the left of that
        index is correct. If the current index + 2 is equal to the number there
        then we know something is missing to the left. Treat it as a binary search
        and split the data again until the right is less than the left. Once the right
        is less than the left, we know left is at the index where the number is missing
        Return left + 1"""
    left = 0
    right = len(nums) - 1  # gives the rightmost index
    while left <= right:
        mid = (left + right) / 2  # calculate the mid index
        m_num = nums[mid]
        if m_num == mid+2:  # something is missing to the left of this number
            right = mid - 1
        else: # we know something is missing to the right
            left = mid + 1  # everything to the left is correct

    # left will now equal the index where the number is missing
    # add one to the index to get the number
    return left + 1

# check to make sure the solution is working on all cases, including numbers at the ends
print detect_missing_num(missing59)
print detect_missing_num(missing3)
print detect_missing_num(missing100)
print detect_missing_num(missing1)

