# Given a string s. Return an integer that represents the longest substring
# that does not have repeating characters

# need to talk about how I completed this problem

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    c_set = set()
    curr_max = left = right = 0  # will be used to iterate through the string
    while left < len(s) and right < len(s):
        if s[right] not in c_set: # this will use hash
            c_set.add(s[right])
            right += 1
            curr_max = max(curr_max, right -left)
        else: # currently in the set, might not remove, but eventually will
            c_set.remove(s[left])
            left += 1
    return curr_max
