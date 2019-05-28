# This problem was asked by Facebook.
# Given a function that generates perfectly random numbers between 1 and k (inclusive),
# where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.
# It should run in O(N) time.
# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

# For this problem, we need to break down the two most important facts
# first is that we're only allowed to swap elements
# the second is that we need to rely on the random function for something
# to randomly shuffle the cards
# lastly, we need to remember that the input for the function is an array of cards
# we can think of this as an array of numbers 1-52, and each number will represent
# a number in the deck of cards

# so when I first start thinking of the problem, I am very curious of what I am going
# to use the random function for. Immediately I think of generating a number and this
# will represent the card that we use for the swap. So we need to think of where we want
# to swap the card, and how we can ensure that the card doesn't get swapped again
# to ensure that the function is O(n). To do this, we can generate a random number 1-k
# k will be determined by the number of NON-SWAPPED ELEMENTS. To ensure this we will
# generate the number and then swap to the end of the array. When we swap to the end of the
# array, we will decrement k to ensure that we don't swap it again. We will keep doing this
# until k is equal to 1, and now the array is SHUFFLED. This is very similar to heap sort
# (if you've learned about it you can think of the decrementing of the non-sorted array
# as the decrementing of the non-shuffled array). All you need to do is implement it now
# and WE'RE DONE

# lastly, to prove that every permutation is equally as likely, we can think of it as choices
# we can think of it as we're filling spots as we go down the line, so there is initially len(n)
# choices, then len(n-1), len(n-2), and as we keep filling spots we get down to 1. Using the multiplication
# rule, we then multiply all of the choices up and get n!. Ensuring that there is an equal opportunity
# for all n! sequences.

import random


def card_shuffle(cards):
    """
    Shuffles a deck of cards that is represented by an array
    :param cards: array with cards
    :return: shuffled deck of cards
    """
    unshuffled = len(cards)  # number of cards that are still unshuffled
    while unshuffled > 1:
        shuffle_i = random.randint(0, unshuffled)
        unshuffled -= 1
        swap(cards, unshuffled, shuffle_i)
    return cards


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# test to make sure it's working
c = [x for x in range(52)]
card_shuffle(c)
print(c)
