# You are a renowned thief who has recently switched from stealing precious metals to
# stealing cakes because of the insane profit margins. You end up hitting the jackpot,
# breaking into the world's largest privately owned stock of cakes—the vault of the Queen of England.
#
# While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.
#
# Each type of cake has a weight and a value, stored in a tuple with two indices:
#
# An integer representing the weight of the cake in kilograms
# An integer representing the monetary value of the cake in British shillings
# For example:
#
#   # Weighs 7 kilograms and has a value of 160 shillings
# (7, 160)
#
# # Weighs 3 kilograms and has a value of 90 shillings
# (3, 90)
#
# You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.
#
# Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity,
# and returns the maximum monetary value the duffel bag can hold.


# when I first looked at this problem, I was immediately curious with the numbers that were provided.
# why is the weight important? How do I choose a cake based on the weight and price?
# immediately I started thinking about ratios. To get the most out of the cake, we want to take the
# greatest ratio of price/cake. If we take the greatest price first and fill our bag with
# as much of this as possible, we can then move down the line to the next most expensive
# cake and start filling our bag with the next cake. Another way that this can be done
# is to create an array of size capacity O(cap), and have each index represent the max value
# of cakes that can be taken for that capacity. Although I do not solve it this way, I encourage
# you to try the DP solution out for yourselves

# to solve this problem, I sort the list in descending order based on the price/weight ratio
# to avoid divide by zero errors, I use a lambda that checks to see if the weight is zero
# and uses maxsize as the comparator instead, because these cakes will have infinite worth
# Note that the sort is in descending order, because we want to iterate through the
# greatest price/weight ratio cakes first. Next, I iterate through each cake in the list.
# I then try to add the cake to the bag if there is enough room. If there is enough room
# I add the cake price to my current running price and then to my current sack weight as well
# What happens if I can add this cake again? To take care of this, a while loop is used
# to ensure that we can put more than one of the same cake in the bag if possible.
# Lastly, the price is returned to the user. This will run in O(nlogn) time where n
# represents the number of cakes in the bakery (this time comes from sorting which is more expensive than the
# last iteration through the list)

import sys


def max_duffel_bag_value(cakes, capacity):
    """
    Takes a list of cakes and a capacity and then
    returns the maximum value that can be stolen
    :param cakes: list of (weight, price) tuples
    :param capacity: max capacity for duffel bag
    :return: integer representing the max price
    """
    curr_w = 0  # current weight of the bag
    price = 0
    cakes.sort(reverse=True, key=lambda c: c[1]/c[0] if c[0] else sys.maxsize)
    for cake in cakes:
        if cake[0] == 0: return sys.maxsize  # infinite number of cakes can be taken
        while (curr_w + cake[0]) <= capacity:
            curr_w += cake[0]
            price += cake[1]
    return price


# possible cake lists
laCakes = [(7, 160), (3, 90), (2, 15)]
zeroWeight = [(0, 5), (8, 100), (1, 20)]

print(max_duffel_bag_value(laCakes, 20))  # example problem
print(max_duffel_bag_value(zeroWeight, 1))  # showing zero weight cakes have inf wealth
