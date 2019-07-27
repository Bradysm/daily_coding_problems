# This problem is relatively easy to do not in place
# simply take the word and split the word at the whitespace
# you can then iterate over the words that were split in reverse order
# and then join the split words on a whitespace. bada boom bada bang

# O(s) time and space, where s is the length of the string

def reverse_words(s: str) -> str:
    return ' '.join(reversed(s.split(' ')))

word = "hello world here"
print("reversed: \'{w}\'".format(w=reverse_words(word)))