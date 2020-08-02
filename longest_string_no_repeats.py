"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

Here is an example solution in Python language. (Any language is OK to use in an interview, 
though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10

Can you find a solution in linear time?


ANSWER:
This is a classic problem where the two pointer technique comes in. We will use two pointers
The left pointer will represent the last (or first letter closest to the beginning of the string)
that is within the current substring that we're looking at. We will then use the second pointer (the faster one)
to move down the substring and add characters into the substring that we're "looking at". As we add characters
into the substring that we're looking at, then we will add the character into the seen set. (Note that although
we are using space the upperbound of characters is finite and will not depend on the input so its O(1) space actually!)

Great! So we move down the string, and decide to add into the set. But what happens if it's in the set already?
Then what we do is remove the value in the set that the left pointer is pointing to and move it up one within
the string. Then to get the length we take the max of the current max substring length and the distance
between the left and the right pointer
"""


def length_of_longest_substring(s) -> int:
    # empty string
    if not s: return 0

    left = right = 0
    longest_substring = 1
    seen = set(s[left])

    # while the pointers are still in the range of the string
    while right + 1 < len(s) and left < len(s):
        # get the next character in question
        next_character = s[right+1]

        # check if the current character is in the seen set
        if next_character not in seen:
            # add the character to the seen set, and move right becuase it's included now
            seen.add(next_character)
            right += 1
        else:
            # remove the left most and move it up one
            seen.remove(s[left])
            left += 1

        # update the longest substring
        longest_substring = max(longest_substring, right - left + 1)

    return longest_substring


test_string = "abrkaabcdefghijjxxx"
print(length_of_longest_substring(test_string))