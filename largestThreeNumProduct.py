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

# we have now decreased the complexity to O(n^2) time and O(1) space!!!! Let's go. And I was able
# to do this in 15 mins which shows so much progress!!! WOOT WOOT. Let's go! Keep you head up and
# keep coding! Cheers, Brady

def three_num_max_product(nums):
    min_pos = nums.index(min(nums))
    max_pos = nums.index(max(nums))
    max_prod = 0

    for i in range(len(nums)):
        for j in range(len(nums)):
            two_product = nums[i] * nums[j]
            if i is not max_pos and j is not max_pos: # we can inlcude max in the product
                max_prod = max(max_prod,  two_product * nums[max_pos])
            if i is not min_pos and j is not min_pos: # we can include the min
                max_prod = max(max_prod, two_product * nums[min_pos])

    return max_prod

nums = [-4, -4, 2, 8]
nums2 = [-1, 10, -100, 5]

print(three_num_max_product(nums))
print(three_num_max_product(nums2))
