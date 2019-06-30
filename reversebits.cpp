/*
Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
so return 964176192 which its binary representation is 00111001011110000010100101000000.

This is another problem that I chose to use C++ because I prefer it for bit manipulation.
For this problem, it's really no different than reversing a strinng. 
You maintain a "bit-pointer" that is used to move down the bits of the numbers and selects the bits
Then you take the bit and place that into the bit location that would be the reveresed location
for that bit. Really, the only thing different than this and reversing a string is understanding the 
masks and bit-wise operations. I'll explain what I did with the mask and bitwise operations below

num: this variable that I created is a 32 bit integer that is filled with all zeros; I used hex because I'm cool
bit_selecet: this is used as a the "bit-pointer" that will "select" bits as it moves down the original number
So the whole premice of this algorithm is to move the bit pointer down using a left shift, select the digit
from n using the and operator (we do this because bit select is a 1 and we want to know if that shift'th bit is a one)
I then right shift it because I prefer to deal with shifting from the 0th place (you can  do the math and not do this)
I then or this with num after I shift it 31-shift to the left. The reason we do a minus is that we want it shift away
from the last left digit when we are reversing a bit that is shift away from the rightmost digit. We then do this
for every digit in the number and BOOM. You have the answer, which by the way is 100% faster than all other solutions
on leetcode...

Please like this repo and follow it if you're enjoying the content! I really appreciate all the support
- cheers, Brady
*/
#include <cstdint>

uint32_t reverseBits(uint32_t n) {
        uint32_t num = 0x0; // start it with 0;
        uint32_t bit_select = 0x1; // used to select bits
        for(int shift = 0; shift <  32; ++shift){
            uint32_t bit = (n & (bit_select << shift)) >> shift; // get the bit
            num = num | (bit << 31-shift); // reverse it
        }
        return num;
    }

