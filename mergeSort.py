# Todays problem was to implement a simple merge sort algorithm
# qucik explination, we want to implement an efficient sort that
# will have a consistent O(nlogn) complexity for best, worst, and average cases
# if you don't know what that is yet, I would go look into algorithm analysis before proceeding

# to gain nlogn complexity, we want to think of splitting the array in half
# and then sorting that half, and then merging the halves together
# we will continutally break the array in half until the array size is 1
# WHAT IS THE NEGATIVE: the negative for this sort is that we need another array
# to implement this sort. It's very challenging to sort them in place, so we
# will create another array of size n to do this

# since we're going to be implementing a divide and conquer technique, it makes
# sense to use recursion

def mergesort(arr):
    """main fucntion for merge sort
       arr - array of unsorted numbers"""
    mergesort_h(arr, ([0] * len(arr)), 0, len(arr)-1)


def mergesort_h(arr, temp, lStart, rEnd):
    """helper function for mergesort
       arr - array of unsorted numbers
       temp - array used for merging
       lStart - start of the current section to be sorted in the array
       rEnd - end of the current section of array to be sorted
    """
    if lStart >= rEnd: return  # current array is of size 1 or less
    mid = (lStart + rEnd) / 2  # calculates the mid of the current array
    mergesort_h(arr, temp, lStart, mid)  # sort the left half
    mergesort_h(arr, temp, mid+1, rEnd)  # sort the right half
    merge(arr, temp, lStart, rEnd)  # merge the left and right halves


def merge(arr, temp, lStart, rEnd):
    """function to merge the left and right halfs of the sorted array
        arr - array of unsorted numbers
        temp - array used for merging
        lStart - start of the current section to be sorted in the array
        rEnd - end of the current section of array to be sorted
    """
    lEnd = (lStart + rEnd) / 2
    rStart = lEnd + 1 # start of the right
    left = lStart  # runner for left
    right = rStart  # runner for right
    tempI = lStart  # stores the current used index in temp

    # merge until one array becomes empty
    while left <= lEnd and right <= rEnd:
        if arr[left] <= arr[right]:
            temp[tempI] = arr[left]
            left += 1
        else:
            temp[tempI] = arr[right]
            right += 1
        tempI += 1  # increment the temp index

    while left <= lEnd: # copy what's left in left array
        temp[tempI] = arr[left]
        left += 1
        tempI += 1

    while right <= rEnd: # copy what's left in right array
        temp[tempI] = arr[right]
        right += 1
        tempI += 1

    # copy over the array
    while lStart <= rEnd:
        arr[lStart] = temp[lStart]
        lStart += 1


# prove that it works
nums = [1, 6, 7, 88, 3, 45, 89, 100, 2, 5, 6]
nums2 = []
nums3 = [1]
nums4 = [1, 5, 3, 4]
mergesort(nums)
mergesort(nums2)
mergesort(nums3)
mergesort(nums4)

print nums
print nums2
print nums3
print nums4

