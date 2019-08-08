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
    reverse(arr, 0, len(arr)-1) # reverse the whole array
    start = 0
    for i in range(len(arr)):
        if arr[i] == ' ' and i-1 >= 0: # check to see if we're on a delimiter
            reverse(arr, start, i-1)
            start = i+1 # place start after the delimiter
    reverse(arr, start, len(arr)-1) # reverse the last word
    return arr
        

def reverse(arr: list, start: int, finish: int):
    while start < finish:
        temp = arr[start]
        arr[start] = arr[finish]
        arr[finish] = temp
        start += 1
        finish -=1
    
word
word_list = [c for c in word]
print("".join(reverse_words2(word_list)))