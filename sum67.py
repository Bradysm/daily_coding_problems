# this is a really trivial problem, although it's marked as a medium

# QUESTION
# Return the sum of the numbers in the array, except ignore sections of
# numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
# Return 0 for no numbers.

# you could also do this in 2 passes and initially sum the whole array and then go through and subtract
# but I assume that the person interviewing wouild prefer one pass since it can be done very easily
# simply check to see if we've seen a six before the number (once we hit a seven "we no longer have seen a six")
# if the number is a 6, then set seen_six to true because this is a new subsequence that is started by the six
# Then check to see if we've not seen a six, and add the number to the sum if that's the case. Lastly, we then 
# check to see if the number is a 7 after checking if we've seen six becuase if we do this before and flip to not seen
# then we will end up adding seven to it after. You could also probably maneuver the logic around, but this just made
# sense to me.

# cheeers,

# Murphy

def sum67(nums):
  total_sum = 0
  seen_six = False
  for n in nums:
    if n is 6: seen_six = True # say that we've seen a six
    if not seen_six: total_sum += n 
    if n is 7: seen_six = False # check after potentially adding whether it's a seven
  return total_sum