# Good morning! Here's your coding interview problem for today.

#This problem was asked by Amazon.

#Given a string, determine whether any permutation of it is a palindrome.

#For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. 
# daily should return false, since there's no rearrangement that can form a palindrome.

# This problem has the ability to become hard because people overthink the problem. When they see it,
# they immediately think of the permutation problem and try to generate all possible permutations and 
# then check to see if that permutation is a palindrome. This is extremly niave and will create
# a factorial time complexity which makes any serious software engineer want to barf. We can 
# reduce this time complexity to O(N) and O(1) space using something called a frequency counter.
# So when you look at all palindromes, they have a couple characteristics, but the one that
# we care about the most is that all valid palindromes have at most one character that has an odd
# frequency. So that means that there can only be one character that is contained in the string
# that occurs an odd number of times. Now lets look at how a frequency counter can help us. We can
# go through the string and increment the frequency of that character within the frequency counter.
# Since we assume a fixed sized alphabet, this will be O(1) space. You can then implement this with 
# an array and map the ascii values of the character to an index within the array. I'm going
# to use a Counter object for simplicty purposes, but I encourage you to try it with an array as well

# Once we get all the characters frequencies, we then check to make sure there is only one character
# with an odd frequency. If there is more than one, then we return false, if there is one or less, then
# we return true

from collections import Counter

def permutation_palindrome(string):
    return valid_odd_frequencies(Counter(string))

def valid_odd_frequencies(counter):
    valid = True
    seen_odd = False
    for f in counter.values():
        is_odd = True if f % 2 == 1 else False
        if is_odd: # check if odd
            if not seen_odd: 
                seen_odd = True
            else: # seen odd already, not valid
                valid = False
    return valid


print(permutation_palindrome("carrace"))
print(permutation_palindrome("abbcad"))
print(permutation_palindrome("daily"))