# Hi, here's your problem today. This problem was recently asked by Microsoft:

#You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

#Example:

#[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

# okay, so this problem has a little bit of trick that comes with it. Right away, you know you can 
# do this in O(N^3) time. That's pretty simple. Just create three loops and find the greatest multiple
# great, but not great! Then, I was thinking to myself, since I've been doing so much DP
# why don't I create a matrix that has all the products of pairs of two numbers from the array
# then I can loop over this matrix and multiply these numbers by the numbers in the array again...
# wait that's N^3 as well... okay, let's keep thinking about this matrix, what numbers do I really 
# want to try multiplying when I get to this product. I always want to check multiplying the greatest
# number and the smallest number in the array of numbers. The reason we check the smallest number
# is because of negatives. By including negative numbers, we have to take into account that the first
# two numbers that create a product might become negative, but that number can then be made
# postive by multiplying a very small (extremly negative) number to that product. So then I thought
# wait a minute, by using this idea of the matrix, I don't actually need to store all of the products
# anymore, I can keep the intuition that I'm using a matrix, but when I get the two sums, I check
# to see if I am using the index that contais the max_i position or the min_i position, I then
# multiply it through if I'm not using one of those and take the max with my current max product!!!

# we have now decreased the complexity to O(n^2) time and O(1) space!!!! But wait, can we do better...

def three_num_max_product(nums):
    min_pos = nums.index(min(nums))
    max_pos = nums.index(max(nums))
    max_prod = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            two_product = nums[i] * nums[j]
            if i is not max_pos and j is not max_pos: # we can inlcude max in the product
                max_prod = max(max_prod,  two_product * nums[max_pos])
            if i is not min_pos and j is not min_pos: # we can include the min
                max_prod = max(max_prod, two_product * nums[min_pos])

    return max_prod

nums = [-4, -4, 2, 8]
nums2 = [-1, 10, -100, 5]
nums3 = [-1, 20, 100, 2, 5, -3, -10]

print(three_num_max_product(nums))
print(three_num_max_product(nums2))
print(three_num_max_product(nums3))

# but then wait, let's think about why we just stored the max and the mins of the number
# when we went through to get the greatest product? When we compute the max product,
# the max product will be the product of the THREE LARGEST numbers, or the largest number
# and the TWO SMALLEST numbers. The reason it's the two smallest and not the three smallest
# is because let's say we have three negative numbers, the product will now also be negative
# so this doesn't help us at all. But if we take the two smallest, and multiply the number
# by the largest in the array, then we get the largest product (of course taht being that)
# the two smallest's product is greatest than the second and third greatest. Okay, so what is
# the best way to keep track of these? We can use a max heap for the smallest numbers
# and a min heap for the largest numbers, We then get to a number and check to see if it's 
# less than the greatst of the min numbers, if so, we replaces that number and reheapify.
# for the min heap, we check to see if the number is greater than the smallest number in the 
# min heap, and we replace and heapify based on that. Okay, great. We can now take the 
# product of the max heap and the largest number in the min heap and then we can max that
# with the product of the min heap. Let's do that! BTW this will be O(1) space and O(N) time
# because the heap size does not depend on the input. No matter how big the input grows,
# the heap size will always be 3 adn 2. If you don't understand that, then look at big O documentation

import heapq

def product(arr):
    if len(arr) == 0 or not arr: return 0
    result = arr[0]
    for x in arr[1:]:
        result *= x
    return result


def max_triple_prod(nums):
    smallest_heap = [] # max of the mins (we multiply by negative 1 to allow us to use min heap still)
    largest_heap = [] # mins of the maxs

    for num in nums:
        if len(smallest_heap) < 2:
            heapq.heappush(smallest_heap, (-1*num))
        elif smallest_heap[0] < num*-1:
            heapq.heappushpop(smallest_heap, (-1*num))
        
        if len(largest_heap) < 3:
            heapq.heappush(largest_heap, num)
        elif largest_heap[0] < num:
            heapq.heappushpop(largest_heap, num)
    
    return max(product(largest_heap), product(smallest_heap) * max(largest_heap))

print('second style')
print(max_triple_prod(nums))
print(max_triple_prod(nums2))
print(max_triple_prod(nums3))
        

