# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# Example 1:
#
# Input: "A"
# Output: 1
# Example 2:
#
# Input: "AB"
# Output: 28
# Example 3:
#
# Input: "ZY"
# Output: 701

# The key to this problem is recognizing the multiple, and understanding that as you move
# right to left, you want to multiply your multiple by 26. I guess that acts as like
# the base for the characters. So it's almost like you're using base 26. Pretty interesting.


def titleToNumber(s: str) -> int:
    val = 0 # initial value
    multi = 1
    for c in reversed(s):
        val += multi * (ord(c ) -64)
        multi *= 26
    return val