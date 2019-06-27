# This problem was asked Microsoft.
# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
# For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

# from what it looks like read7 handles there being nothing left to read in a file. So let's not worry
# too much about that and focus on what is going on with the reading
# Lets first look at how many reads we need for the number n. let's assume n > 7 initailly. So for n > 7
# there will be n/7 reads where we use the whole output from read7. Then there will be one last read (assuming n%7 != 0)
# where we only partially use the string that is returnned from read7. More specifically, we will use n%7 characters from it

# if n is < 7, then we will perform n/7 full reads (or zero) and use n characters from read7.
# So, we know how to throw this function together


def readN(n: int, read7) -> str:
    result = ""
    full_reads = n/7  # number of full reads
    while full_reads > 0:
        result += read7() # read 7 characters
    # add the last characters
    return (result + read7()[:n%7]) # concatinate and return