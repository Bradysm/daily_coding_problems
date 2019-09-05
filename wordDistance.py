# Good morning! Here's your coding interview problem for today.

# Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

# For example, given words "hello", and "world" and a 
# text content of "dog cat hello cat dog dog hello cat world", 
# return 1 because there's only one word "cat" in between the two words.

# O(w) space where w is the number of words and the time complexity is O(w*s) where s is the longest word inputted from word1 and word2
# due to the comparisons of the words. Note that this uses the simple "two pointer" technique
import sys
def word_distance(string, word1, word2):
    # split the string at the space
    w1_i = w2_i = -1 # start them at -1 for not being seen
    distance = sys.maxsize
    for i, w in enumerate(string.split(' ')):
        # update w1_i or w2_i if is the same 
        w1_i = i if w == word1 else w1_i # update the w1_i
        w2_i = i if w == word2 else w2_i # update the w2_i
        both_words_seen = True if w1_i is not -1 and w2_i is not -1 else False
        
        if both_words_seen:
            distance = min(distance, abs(w1_i - w2_i)-1)

    return distance



print(word_distance("dog cat hello cat dog dog hello cat world", "hello", "world"))