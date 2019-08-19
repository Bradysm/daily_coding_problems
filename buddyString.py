# Hi, here's your problem today. This problem was recently asked by AirBNB:

#Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

#Example 1:
#Input: A = "ab", B = "ba"
#Output: true

#Example 2:
#input: A = "ab", B = "ab"
#Output: false

#Example 3:
#Input: A = "aa", B = "aa"
#Output: true

#Example 4:
#Input: A = "aaaaaaabc", B = "aaaaaaacb"
#Output: true

#Example 5:
#Input: A = "", B = "aa"
#Output: false
from collections import Counter
def buddy_string(s1, s2):
    # if they aren't the same length then it's not possible
    if not len(s1) == len(s2) or len(s1) < 2 or len(s2) < 2: 
        return False 
    # not the same number of characters O(1) space because fixed size alphabet
    if not Counter(s1) == Counter(s2):
        return False

    # fille up a character index map
    s1_map = {c:[] for c in s1}
    for i in range(len(s1)):
        s1_map[s1[i]].append(i)

    # for every O(n*f) where n is the number of characters and f is the frequency of repeats of those characters
    for j, c in enumerate(s2):
        for i in s1_map[c]: # get the list of indexes from s2:
            if i is not j and swapable(s1, s2, i, j):
                return True

    return False


def swapable(s1, s2, i, j):
    return True if s1[i] == s2[j] and s1[j] == s2[i] else False

print(buddy_string("aaaaaaabc", "aaaaaaacb"))
print(buddy_string("ab", "ab"))
print(buddy_string("", "ab"))
print(buddy_string("aa", "aa"))