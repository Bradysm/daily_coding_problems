"""
Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. 
Do not convert the integer into a string.


So, for this problem, we will convert the number an array by moding the first
digit off, and then placing it in an array and then dividing by 10 to shift
the rest of the digits down. Once the number is equal to zero, then we will
run a palindrome check on the array of digits

This will run in O(log_10(n)) where n represents the number passed in
This space will also be O(log_10(n)) or O(d) where d represents the number
of digits in the number, n
"""

def palindrome_number(n) -> bool:
    digits = []

    # create the array of digits
    while n:
        digit = n % 10
        digits.append(digit)
        n //= 10 # integer divide

    # check to see if palindrome
    left = 0
    right = len(digits) - 1
    palindrome = True

    while left < right:
        # check to see if the digits are the same
        if digits[left] != digits[right]: 
            palindrome = False
        
        # move the pointers
        left += 1
        right -= 1 
    

    return palindrome


# run tests
print("678", palindrome_number(678))
print("6786", palindrome_number(6786))
print("8", palindrome_number(8))
print("89998", palindrome_number(89998))
