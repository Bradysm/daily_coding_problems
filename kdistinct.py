"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

I have no idea why this problem is considered hard? Maybe it's all perspective and maybe I could just be wrong
The way I see this is we use a fast and slow pointer, and then move down the string and keep a set of characters.
Once the set is at size k, then we can add no new characters and are forced to remove from the left side. The only
issue with using a set though, is that we don't know the number of times that the character is within that
substring, so maybe using a map that will contain the count of the characters within that substring and then use
an int to count the current number of characters within that substring. And then that will allow us to check
the number of characters. I guess you could also use the length of the numebr of keys, since there are only guarunteed
26 keys, that is technically O(1), but im not too sure how that implementation is done within the dictionary DS in python
I guess, we will just use that and then call it a day from there. Let's do it
"""

from collections import defaultdict

def longest_substring_k_distinct(s, k) -> int:
    if not s: return 0

    # max length
    max_lenth = 1    
    
    # create a counter and set the first character count to 1
    counts = defaultdict(int) # set the first character to a count of 1
    counts[s[0]] += 1
    num_characters = 1

    # create fast and slow pointers
    slow = fast = 0 # assume that the left pointer shows what is currently contained and the next index of the right pointer is what is in question

    while slow < len(s) and fast + 1 < len(s):
        # get the next character
        next_char = s[fast+1]
        
        # if the number of characters is less than k, then add
        if num_characters < k:
            num_characters += 0 if counts[next_char] is not 0 else 1
            counts[next_char] += 1

            # move the fast pinter
            fast += 1
        else: # current number of characters is equal to k
            if counts[next_char] is 0: # the next character is not in the counts
                # move the slow
                counts[s[slow]] -= 1
                num_characters -= 1 if counts[s[slow]] is 0 else 0 # remove total numbers if the character removed removed the last character
                slow += 1
            else:
                counts[next_char] += 1
                fast += 1

        max_lenth = max(max_lenth, (fast + 1 - slow))

    return max_lenth


print(longest_substring_k_distinct("abcba", 2))