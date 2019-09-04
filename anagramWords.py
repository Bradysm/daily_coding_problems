# Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).
# Example:
# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

# O(n*a) time complexity and O(n) space
from collections import Counter
def anagram_words(words: list) -> list:
    anagram_dict = dict()
    for word in words: # O(N)
        found = False
        for key in anagram_dict.keys(): # O(a) where a is the number of anagrams
            if Counter(word) == Counter(key): # assuming we have a fixed character set, this is O(1)
                anagram_dict[key].append(word)
                found = True
        # check to see if we didn't find an anagram
        if not found: anagram_dict[word] = [word]

    # concatinate all of the keys into a list
    return [lst for lst in anagram_dict.values()]

print(anagram_words(['abc', 'bcd', 'cba', 'cbd', 'cab', 'efg']))
