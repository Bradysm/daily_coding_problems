"""
This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1. 
Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.


Here is my thought process. Assume we have n numbers with n probabilities.
Let's say that we have a set of boxes, that represent the numbers and their
probabilites. That would mean that each number would have a proportional number
of boxes to the total number of boxes to assure that the probability of you choosing
that box is equal to the probability of that number. I then took this idea and assumed
that we could have 100 boxes. Then, based on the probability of the numbers. I would
then assign each number their respective box count. So if 1 had a probability of 0.1,
then it would take up 10 boxes. I then did this for each of the numbers to get the 
total probability of 1, or 100 boxes. Then, I used the fact that we could generate
a random number from 0-1 to get the index of the number that we chose. We would then
multiply the random number by 100 and reach into the box and return that number (or
simply look into the array and return the number that is stored at that index).

I do realize that my implementation could run into some errors when the rounding
of the probabilities doesn't work out right and might have an array of size 99,
but you select the 100th box. This is an issue that i need to handle. When I look
back over this problem.

This takes O(1) space since the array does not depend on the size of input, and
takes O(n) time becuase we need to go through each of the numbers in the input.

"""
from random import seed, random
from collections import Counter


def n_number_probability_generator(nums, probabilities) -> int:
    """
    Takes the numbers and their respective probabilities and returns
    the numbers
    """
    prob_array = [nums[0]] * 100
    curr_index = 0
    
    for num, prob in zip(nums, probabilities):
        # calculate the number of array indexes to give the number
        number_of_slots = int(prob * 100)

        # update slots in probability array
        for i in range(curr_index, curr_index+number_of_slots):
            if i < len(prob_array): prob_array[i] = num

        # update where we are in the probability array
        curr_index = curr_index + number_of_slots

    # pick a random index
    random_index = int(100 * random())
    return prob_array[random_index]



# test script
test_nums = [1, 2, 3, 4]
test_probabilities = [0.1, 0.5, 0.2, 0.2]
test_runs = 10_000

counter = Counter()
for iteration in range(test_runs):
    counter[n_number_probability_generator(test_nums, test_probabilities)] += 1

for num, count in counter.items():
    print("{num}: {prob}".format(num=num, prob= count / test_runs))


"""
My results:

1: 0.1032
4: 0.1995
2: 0.4971
3: 0.2002
"""