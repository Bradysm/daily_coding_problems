# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array,
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
#8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space.
# You can modify the input array in-place and you do not need to store the results.
# You can simply print them out as you compute them.
# assume len(lst) >= k


# the key to solving this problem is recognizing that you're consistently moving down
# the list by removing the left most from the k values and inserting the right most
# into the comparison. As a result, the data structure that would fit this would
# be a queue, as it's insertion on one end, and deletion on the other. Since we're
# allowed to use O(k) space, which will be the size of the queue. We will fill the
# queue with the initial k items, take the max, and then remove from the front and
# add to the end to get the next max of k. This process will repeat until there
# are no more numbers to add to the queue


def k_maxs(lst, k):
    """
    :param lst: list of numbers
    :param k: increment of numbers that we compute the return of
    :return: none, mins are printed
    """
    queue = [lst[i] for i in range(k)]
    lst = lst[k:]
    for num in lst:
        # print the min of current k, remove front add back
        print(max(queue))
        queue.remove(queue[0])
        queue.append(num)
    # print the final min
    print(max(queue))


# space used for testing
lst1 = [1, 3, 5, 2, 8, 100, 3, 6]
lst2 = [10, 5, 2, 7, 8, 7]
k_maxs(lst1, 3)
print("next k_min")
k_maxs(lst1, 5)
print("their test")
k_maxs(lst2, 3)
