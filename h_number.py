"""
Hi, here's your problem today. This problem was recently asked by Amazon:

The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar.
 The definition of the h-index is if a scholar has at least h of their papers cited h times.

Given a list of publications of the number of citations a scholar has, find their h-index.

Example:
Input: [3, 5, 0, 1, 3]
Output: 3
Explanation:
There are 3 publications with 3 or more citations, hence the h-index is 3.

Solution:
sort all of the papers based on their citations
Then we start from the beginning and check to see if the citation number is greater
than or equal to the total number of citations minus the citations before that current
publication (which is equal to the current index). We then do this up until the end,
and have achieved the h_index
"""

def calculate_h_index(citations) -> int:
    # sort from least to greatest citations o(nlogn)
    citations.sort()

    # one liner, the extra space wouldn't matter if merge sort was used because there would be extra space needed for the merge
    #return max([citation if (len(citations) - i) >= citation else 0 for i, citation in enumerate(citations.sorted())])

    h_index = 0
    num_publications = len(citations)
    for i, citation in enumerate(citations):
        h_index = citation if (num_publications - i) >= citation else h_index

    return h_index

# test cases
print(calculate_h_index([3, 5, 0, 1, 3]))
print(calculate_h_index([3, 5, 0, 1, 3, 4, 4, 6]))
print(calculate_h_index([0, 1, 3, 1]))