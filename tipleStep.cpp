/**
 * A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
 * Implement a method to count how many possible ways the child can run up the stairs
 * 
 * 
 * So whenever you see a problem with "calculate the number of possible ways to..."
 * you want to think of a recursive / dynamic programming problem
 * 
 * For this problem, it's nice to start at the top stair and act like you're jumping backwards
 * So we start at the nth step and take jumps backwards with all possibilities.
 * Then we do that from the next step, and so on. We can do this completely recursively
 * without any memoization, and this would take O(3^n) timecomplpexity because we have three
 * directions to branch from for every node in the tree. But to decrease the time complexity
 * we can store a vector (or array or whatever you want to call it in your language)
 * to carry the values for each step once they're computed. Thus, when the call happens again for
 * that specific step, we can simply do O(1) work by getting the value from the vector.
 * 
*/
#include <iostream>
#include <string>
#include <vector>

// prototype for function
int tripleStep(int i, std::vector<int> s);
int tripleStep(int n);

int main(){
    int step; // variable to be used

    std::cout << "How many steps are we climbing: ";
    std::cin >> step;


    // calculate the number of possible ways the child can step
    std::vector<int> s(step+1, -1);
    std::cout << "The child can step: " << tripleStep(step) << std::endl;
}

/*
Top-down solution
int tripleStep(int i, std::vector<int> s){
    if(i < 0) return 0; // you can't make any movements from here
    if(i == 0) return 1; // we reached a valid step sequence
    if(s[i] != -1) return s[i]; // check to see if we already calculated the value
    
    // calculate the number of sequences to get to step i
    s[i] = tripleStep(i-1, s) + tripleStep(i-2, s) + tripleStep(i-3, s);
    return s[i];
}
*/

/*
Create a bottom-up solution
*/
int tripleStep(int n){
    int first = 1; // from the first step
    int second = 2; // from the second step
    int third = 4; // from the third step
    for(int i = 4; i <= n; ++i){
        int z  = first + second + third;
        first = second;
        second = third;
        third = z;
    }
    return third;

}