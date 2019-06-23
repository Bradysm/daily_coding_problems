# given a roman num, return the value of the roman numeral

# the key here is to create a dictionary to map all the values of the letters
# iterate through the string, and only subtract the value from the number
# after it if the number before is smaller. They give some descriptions
# on the only numbers that can be decremented, but any valid roman
# numeral would stick to the more simple description I just gave.
# (question given on leetcode mock interview)
# passed all tests


def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    # used as a mapping for the values
    numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0
    i = 0
    while i < len(s):
        # check to see if we should decrease the value
        if i+1 < len(s) and numeral[i] < numeral[i + 1]:
            val += numeral[i + 1] - numeral[i]
            i += 2
        else:
            val += numeral[i]
            i += 1

    # return the roman num
    return val

