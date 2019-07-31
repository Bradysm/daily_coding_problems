# Given an array of positive integers representing coin denominations and a single non-negative integer representing a 
# target amount of money, implement a function that returns the smallest number of coins needed to make change for that 
# target amount using the given coin denominations. Note that an unlimited amount of coins is at your disposal. 
# If it is impossible to make change for the target amount, return -1.

# Okay, so when you see this problem, like I did, you probably thought, okay, let me just take the largest denom
# denom, divide out that number the most times, then move onto the next largest and so on, and that will
# get my answer. Yes that will work if you're give the current US coin system, but what if I gave you the
# values [3, 7] and the number 9 to count change for? You would divide out 7, then you would have remainder 2
# and then you would say that it wasn't possible and move on with your day WRONG

# When I saw this problem you want to count the nth number of coins needed to make change. So I immediately started
# thinking of recursion and DP. If you see that you need to calculate the nth number of soemthing, see if you can 
# create a recurrence relation for calculating the kth number. For this, the kth value will be the T(k) = min(T(k-coin_vak), T(k))
# because if we take away the coin value from the current value that we're at, then we have T(k-coin) to find the 
# smallest nuber of change for. If we minimize the smallest number of coins as we build the solution up,
# then by acting optimally, we will get the optimal solution of the min number of coins

# Once I realize the recurrence relation, I then draw out a 2D array, down the rows I put the coin denominations
# and acrosse the columns I put the values from 0-n (so the size of the matrix is coins*(n+1)). Once we have that
# we can then take the current denomination that we're at, and move down it's row, if the current i-coin_val == 0 or 
# the element for any of the denominations for that column are not -1 (we initiallize the matrix to -1) Then
# we add one to that value and set the current element to the min of the current and the number of coins we just computed

# notice that we store a lot of vlaues that are -1 and we have to move down the columns for previously computed
# values, but more so even notice that we only care about the smallest value in that column, so we then
# can crush this matrix into a 1-dimmensional array that will contain the min number for that number of change 
# for these denominations. We then continue the same computation except we don't have to find the min in the column
# that is not equal to -1. We still act optimmally by setting coins[i] = min(coins[i], 1+ coins[i-coin_val])

# this will now give us O(n*d) time and O(n) space. Where d is the number of denomination and n is the 
# change value that we're computing

def minNumberOfCoinsForChange(n, denoms):
	coins = [-1] * (n+1) # create an array of n+1
	coins[0] = 0 # set the zeroth index to zero
	for coin in denoms: # for every coin, try each index up to it
		for i in range(coin, len(coins)): # go for every index
			if (i-coin) >= 0 and (not coins[i-coin] == -1):
				num_coins = 1 + coins[i-coin]
				coins[i] = num_coins if coins[i] == -1 else min(coins[i], num_coins)
				
	return coins[-1] # will be -1 if there are no ways to make it