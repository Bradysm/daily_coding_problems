# a b c v a b b v c a
# 0 0 0 0 1 2 0 0 0 1

def failure_function(s):
    pre = 0
    suff = 1
    pre_arr = [0] * (len(s)+1) # create the prefix function
    while suff < len(s) and pre < len(s):
        if s[pre] == s[suff]:
            # continued prefix
            pre_arr[suff+1] = pre + 1
            suff += 1
            pre += 1
        else:
            # restart prefix counter
            if pre == 0:
                suff += 1
            pre = 0

    return pre_arr

def kmp(s, pattern):
    if len(s) == 0 and len(pattern) == 0: return True # both are empty
    if len(pattern) == 0 or len(s) == 0: return False # once of them is empty

    # we're looking for pattern within string
    pre_arr = failure_function(pattern) # get the prefix array
    pattern_i = str_i = 0 # set them both equal to zero
    # search for the string within
    occurrences = []
    for i in range(len(s)):
        while not pattern_i == -1:
            



    while str_i < len(s): # continue searching as long as there is more string to search 
        if s[str_i] == pattern[pattern_i]: # they're equal
            pattern_i += 1
            str_i += 1
            if pattern_i == len(pattern):
                occurrences.append(str_i - pattern_i)
                pattern_i -= 1 # move to potential prefix
        else:
            # check to see if we checked the beginning
            # update on the prefix table
            pattern_i -= 1
            if pattern_i == -1:
                str_i += 1
                pattern_i = 0
            else:
                pattern_i = pre_arr[pattern_i]
            
    return occurrences


print(kmp("abcvaaaavava", "aa"))
#print(failure_function("aa"))
#print(failure_function("abcvaaaavca"))

# str_i = 0->1->2
# pattern_i = 0->1->0