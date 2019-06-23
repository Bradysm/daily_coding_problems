# Given a string and a string dictionary,
# find the longest string in the dictionary that can be formed by deleting some characters of the given string.
# If there are more than one possible results, return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.
#
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000

# Immediately when I saw this question, I was a little nervous. The reason being is that
# I tend to be not as good with string problems as I am with other problems. BUT, this
# means I just need to work on them more, so here we go. I'm going to describe two different
# solutions for this problem.

# the first solution is a brute force solution. You've probably seen this in all kinds of
# interview problems on this repo, but it's thinking of teh solution like a powerset.
# we get to each character and thn choose to either add it to the list or not. We then
# check to see if that list matches on of the words in the dictionary and make the
# current word equal to that word. Then choose to not add it and update the current
# word if the word that didn't add it is longer or is the same length and lexiographically
# less than the currennt word. Sheesh. This will be O(2^n) time and O(n) space due
# to the stack space needed for recursion. The 2 comes from the node at each branch in the
# recursion tree branching by a factor of 2 due to adding and not adding the value

# That was a lot. Okay, now let's get to the arguably
# more simple solution that.
# My problem with initially solving this was that I was going to user a counter and then
# just make sure that the string s had >= the number of that specific character needed
# in the word. The problem that I ran into is that it's not just about the correct number,
# but also the order. That got me thinking. What if we had two "pointers" for each string
# we then move down the string s and as we move down, we check if the character at s[i] is the
# same character at word[j]; if it is, increment j because we found that character in the correct order
# We always increment i because we're passing down s, so no matter what we increment i. Then I had to think
# about the conditions for the loop. We want to stop when we've seen all the characters in word, or if
# we ran out of characters in s, so that is a simple condition to meet. You then update the max
# word if the current word is longer. I then added a little code tuning by just continuing if the current
# word that we're on is < len(m_word). This is because no matter if we found that word, it wouldn't replace
# m_word. BOOM, we now have a Olen(dic)*max(words)) complexity and are using O(max(word))


def findLongestWord(s, d):
    m_word = ""
    for word in d:
        w_len = len(word)
        if w_len < len(m_word): continue
        s_index = w_index = 0  # indexes for the two strings
        while w_index < w_len and s_index < len(s):
            w_index = w_index + 1 if s[s_index] == word[w_index] else w_index
            s_index += 1
        #  found all characters
        if w_index == w_len:
            if w_len == len(m_word):
                m_word = min(m_word, word)
            elif w_len > len(m_word):
                m_word = word
    return m_word

