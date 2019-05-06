# This problem was asked by Google.
# The edit distance between two strings refers to the minimum number of character insertions,
# deletions, and substitutions required to change one string to the other.
# Given two strings, compute the edit distance between them.

def edit_distance_help(str1, str2, i, min_len):
    """
    Gives the edit distance between two strings
    :param str1: first string
    :param str2: second string
    :param i: index being compared
    :return: the number of insertions, deletions, and removes to make the same
    """
    # check if we're at the end of shortest length
    if min_len is i: return abs(len(str1) - len(str2))
    change = 0
    if str1[i] is not str2[i]: change = 1
    return change + edit_distance_help(str1, str2, i+1, min_len)


def edit_distance(str1, str2):
    if str1 is None and str2 is None: return 0
    if str1 is None: return len(str2)
    if str2 is None: return len(str1)
    # neither none, calculate edit distance
    return edit_distance_help(str1, str2, 0, min(len(str1), len(str2)))



# prove that it works correctly
print(edit_distance("kitty", "abc"))
print(edit_distance("kitten", "sitting"))
print(edit_distance("brady", "shadyness"))
print(edit_distance("abc", None))
print(edit_distance(None, "abc"))
print(edit_distance(None, None))