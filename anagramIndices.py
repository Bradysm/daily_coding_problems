"""
Given a word w and a string s, find all indices n s which are the starting
locations of anagrams of w. For example, given w = ab and s = abxaba, return [0, 3, 4]


So the first thing to think about is what an anagram is? A string is an anagram
if it contains the same number of distinct letters. So for the case in the
example above, the anagram would be if there was 1 a and 1 b in the substring
starting at index i and ending at i+1

What does counting for us? Well we can think of counting with a dictionary,
this would allow us to pass through in O(k) time but would take O(k) space
where k = len(w). Another approach is to sort the strings and then compare the
strings, this would take klogk time (assuming you use qsort or another sort
with this time complexity). The trade-off of time and space will have to be
decided based on the function that you're designing. I will choose to use
the counter version
"""

# import a counter dictionary
from collections import Counter


def is_anagram(s1, s2):
    """
    This function will decide whether the two strings
    are anagrams of eachother
    :param s1: string 1
    :param s2: string 2
    :return: true if they're anagrams of eachother
    """
    if len(s1) is not len(s2): return False
    return Counter(s1) == Counter(s2)


def ana_indices(w, s):
    """
    Function returns a list containing the indices that are
    an anagram of w.
    :param w: word that is used for anagram
    :param s: string containing letters that will be indexed
    :return: list containing indexes that are
    """
    indices = []
    # iterate through indices that will allow len(w)-1 strings from there
    for i in range(len(s) - (len(w)-1)):
        # create the substring
        sub = s[i:i+len(w)]
        if is_anagram(sub, w):
            indices.append(i)
    return indices


# testing
print(ana_indices("ab", "abxaba"))
print(ana_indices("he","helloeh"))
print(ana_indices("", "world"))  # every index is an anagram
print(ana_indices("word", ""))  # test on an empty string
