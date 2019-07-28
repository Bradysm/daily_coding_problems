# This problem is relatively easy to do not in place
# simply take the word and split the word at the whitespace
# you can then iterate over the words that were split in reverse order
# and then join the split words on a whitespace. bada boom bada bang

# O(s) time and space, where s is the length of the string
def reverse_words(s: str) -> str:
    return ' '.join(reversed(s.split(' ')))

word = "hello world here"
print("reversed: \'{w}\'".format(w=reverse_words(word)))


# if we assume that the string is mutable (so this could be an instance where the characters are passed in
# an array) Then we can perform another algorithm to compute this result. The way I thought of this problem
# was to mentally replace all the characters for a word with a placeholder. If we then reverse the list with the
# placeholder, then the placeholder will be in the correct space i.e. the word is in the correct space in the lsit
# we just need to make sure the word is in the correct order. So if we reverse the whole list, then the words will
# be in the correct position. We then make a second pass with two pointers and reverse the words contained
# within the array themselves to get the words in the correct order.

# O(s) time and O(1) space


def reverse_words2(arr: list) -> list:
    # implementation
    return None