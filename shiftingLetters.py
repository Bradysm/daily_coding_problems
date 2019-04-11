# We have a string S of lowercase letters, and an integer array shifts.
# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.
# Return the final string after all such shifts to S are applied.
# Input: S = "abc", shifts = [3,5,9]
# Output: "rpl"

# Although this problem may seem a bit daunting, it is really just a mix of core CS
# concepts that are smushed together to make a medium diff problem
# In my opinion, the key to this problem is realizing that the sum of the shifts
# from i to the end of the list, is the number of shifts applied to that specific
# index within the string. So, we can sum the list of numbers, apply that shift to
# the first letter, then subtract the number at i in shifts from the sum and apply
# that shift to the next number. The last key aspect of this question is that you
# need to understand the "wrap around". Whenever you hear wrap around, think of
# the MOD function immediately. Since there are 26 letters in the alphabet, if
# we treat z as 25, then z + 1 mod % 26 will give us 0 which will be 'a'. We will
# then add this number to ord('a') which will act as the base to be incremented on
# and then add this character to a list of characters. We don't want to keep recreating
# new strings because they're immutable and will load up in memory. Return the joining
# of all of the character as a string and you have the final result.


class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        # create a list so we aren't creating a bunch of strings in mem
        newS = []
        shift = sum(shifts) # sum all of the shifts
        for i, c in enumerate(S):
            newS.append(chr(((ord(c)-ord('a') + shift) % 26) + ord('a')))
            shift -= shifts[i]
        return "".join(newS)