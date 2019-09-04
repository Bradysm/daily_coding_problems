#Hi, here's your problem today. This problem was recently asked by Apple:

#Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.

#Example:
#Input:
#words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

#Output: False
#Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

#Example 2:
#Input:
#words = ["zyx", "zyxw", "zyxwy"],
#rder="zyxwvutsrqponmlkjihgfedcba"
#Output: True
#Explanation: The words are in increasing alphabetical order

# sorry that I'm getting lazy with the explinations. I just signed with Capital One and haven't had
# the motivation to write as much in the comments. Im going to slowly come back to doing interview problems
# I was taking a break because it's so stressful and I just wanted some time to clear my head


# O(n*s) time and O(1) space (this is assuming the character set is constant so the dictionary will always be constant space)
def words_in_order(words: list , order: str) -> list:
    letter_order = {order[i]: i for i in range(len(order))} # create the mapping of the letters to the order they're in
    for word_i in range(1, len(words)):
        word1 = words[word_i-1] # word before
        word2 = words[word_i] # word after
        word1_i = word2_i = 0

        while word1_i < len(word1) and word2_i < len(word2):
            c1_order = letter_order[word1[word1_i]]
            c2_order = letter_order[word2[word2_i]]
            # check if the letter in the second word comes before the first word letter
            if c2_order < c1_order: return False
                
            # move to the next letter
            word1_i += 1
            word2_i += 1
        
    return True

print(words_in_order(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
print(words_in_order(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))
