# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid 
# (i.e. each open parenthesis is eventually closed).
# For example, given the string "()())()", you should return 1. Given the string ")(", 
# you should return 2, since we must remove all of them.

# immediately when I see a problem involving parentheses. I IMMEDIATELY THINK OF USING A STACK.
# the reason for this is that we want to focus on the last thing placed into the stack which is
# the most recent parenthese. This will allow us to make open and closing pairs.
# what we will do here is start with a stack and add to the stack when there is an opening
# parentheses. If it's a closing paren, we will check to see if the length of the stack is > 1
# if it is pop of the end of the stack. If the length of the stack is == 0, then we add one to removed
# because that closing paren cannot be there. Okay, great that's O(n) space and time. Let's do better
# if you noticed we used the stack, but really didn't care about what was in there, we only cared about
# the length because we solely put one paren into it. So, we could exchange the stack for an int called open
# we will then use this as the "stack" and increment it when we see open parens and decrement when we see closing ones
# (assuming it's greater than 0)

# lastly, what if the string contained only opening paren? How would we handle this. Well, after we go through
# all of the parentheses, we will then add the number of remaining open paren to the removed value. This is because
# we will need to remove all of these to make the string valid! Great O(n) time and O(1) space!!!! LETSS GOOOOO

def min_removed(parens):
    """
    returns the number of parentheses that need to be removed to make a valid string
    return: int representing removed paren
    """
    remove = open_paren = 0
    for paren in parens:
        if paren == '(': 
            open_paren += 1
        else:
            if open_paren > 0: open_paren -= 1
            else: remove += 1
    return remove + open_paren


# tests to make sure it works!
print('((((: removed', min_removed('(((('))
print(')(: removed',  min_removed(')('))
print('(()))((: removed', min_removed('(()))(('))
print('()())(): removed', min_removed('()())()'))