/* Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given three 32-bit integers x, y, and b, 
# return x if b is 1 and y if b is 0, 
# using only mathematical or bit operations. You can assume b can only be 1 or 0.
*/
#include <cstdint>
#include <iostream>

/*
Okay, so this problem definitely is more suited towards programmers that have a more "formal"
CS degree. One that involves a little more low level programming and systems courses.
It is not very hard per say, but the concepts are something that you will learn in one of these courses
and I totally would've not known how to do this without my comparch class. Also, note that I chose
to use C++ for this problem because I perfer to do low level problems in non-python programming languages

Anyways, so the key to this problem is understanding bit-shifts and masks, and really you follow
The same procedure for botth the maskings. What I am doing is taking b and then shifting it to the 
right 31 bits, this will then fill the number with trailing zeros and place the LSB in the MSB slot.
I then take the MSB and shift that down 31 bits so the number is now filled with all ones or all zeros.
The key is that left shifting will not carry the LSB where right shifting will carry the MSB. So, we can 
then and this new "mask" with x and with y, so we can either "adopt" that value if our mask is 0xffff or
we will discard it because our mask is all zeros.

Notice the one difference between the x checek and the y check. For the y check, I first negate the
value. This is because when we shift down and back with b being 0, we want the mask to be all 1's.
The only way to do this is to start with a 1 in the LSB. This will then also turn 1 into zero which
creates the all zero mask that we wanted as well.

Lastly, we or the two checks so we get the proper integer to return. This my friends, is how you
make a "proper" ternary function!

*/

int32_t bitmath(int32_t x, int32_t y, int32_t b){
    int32_t xcheck = ((b << 31) >> 31) & x; // this will be all zeros if it was 0, and all 1's otherwise, then and with x
    int32_t ycheck = ((!b << 31) >> 31) & y;
    return ycheck | xcheck;
}

int main(){
    std::cout << "Test b is 1: ";
    std::cout << bitmath(3, 10, 1) << std::endl;
    std::cout << "Test b is 0: ";
    std::cout << bitmath(3, 10, 0) << std::endl;
}
