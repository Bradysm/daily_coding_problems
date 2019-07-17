# Good morning! Here's your coding interview problem for today.
# This problem was asked by Lyft.
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.


# When I first saw this problem, I immediately took the note that the numbers that we're summing must be contiguous
# So, knowing that they must be contiguous, we know that we are summing numbers consitently one after another.
# How can we utilize this? Well, we can use two pointers, one that stores the left most index that is in the sum,
# and a right pointer that stores the right most index that is in the sum (for this problem the right index I choose
# for it to be one after the index for splicing purposes. So if the right most is at i, the i-1 index is in the sum).
# we can then use these pointers to move down the array and collect sums within the array of numbers that we're given.

# First things first, how do we know if a number is included in the sum. Let's take a look at the example to see if
# we can create some cases and how to handle them. So we're at index 0 and we see 1, if we add one to our current
# sum of 0, we will get a total sum of 1 that is less than k, this is still a valid sum so we include it and move
# the right pointer down one. We keep doing this until we get the right pointer to index 3. At this point in tiume
# we will have a total contiguous sum of 6, and the current number in question is 4. If we add 4 to the current sum,
# we will get 10 > k, so this is not valid and we can't add it to our current sum. So what do we do now?

# Since we know the current sum is not valid, the current contiguous array cannot go any further and so we make a change
# to the current sum. To do this, we subtract the leftmost value from the current sum and increment the left pointer.
# not that we still havent added for to the sum, but have just mutated where the start of this contiguous sum starts.
# the contiguous sum is now 5, and we're still at the number 4. We see that adding 4 to it get's us a k of 9 which is what we want!
# Great. Now we still increment the right pointer, because we're using a splicing for my solution, but it's just as valid to
# use a queue and enqueue and dequeue instead. In fact, that will be a solution that I produce. 

def contiguous_sum(nums, k):
    queue = []
    curr_sum = 0
    i = 0
    while i < len(nums) and not curr_sum == k:
        if nums[i] + curr_sum <= k:
            curr_sum += nums[i]
            queue.append(nums[i])
            i += 1
        else: # adding the number will put curr_sum above k
            if queue: # try removing if possible
                num = queue.pop(0)
                curr_sum -= num
            else: # the current number is just too big
                i += 1
    return queue



print(contiguous_sum([1, 4, 3, 5, 2, 10, 9], 9))
print(contiguous_sum([1, 2, 3, 4, 5], 9))

