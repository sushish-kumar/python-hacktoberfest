"""House Robbing Problem: Alice is a skilled thief who plans to rob houses down a lane.
Each house has a certain amount of money stashed, and the only thing keeping Alice
from robbing each of them is that neighbouring houses have security systems attached,
and if two adjacent houses are broken into on the same night, the security systems will 
immediately notify the police. Write a program with dynamic approach in O(n) time complexity, 
which return the maximum amount of money you can steal tonight without alerting the cops, given 
an integer array wealth representing the amount of money lying in each home.
Example : If there as 5 houses in a street, and their wealth array is given as: [2, 7, 9, 3, 1].
Output : 12
Explanation: Rob house 1 (give wealth = 2), rob house 3 (give wealth = 9) and rob 1 house 5 (give wealth = 1). Total profit Alice = 2 + 9 + 1 = 12
"""

def maxLoot(wealth):
    
    n = len(wealth)
    
    #If there is only one house then maximum loot is all the money in that house
    if n==1: 
        return wealth[0]
    
    #dp[i] stores maximum loot possible by robbing till ith house
    dp = [0] * n
    
    #base cases
    dp[0] = wealth[0]
    dp[1] = max(dp[0], wealth[1])
    
    for i in range(2,n):
        
        #The robber either robs ith house or doesn't rob. If he robs then he must'nt have robbed previous house. In that case
        #maximum loot will be dp[i-2] + wealth[i]. If he doesn't rob current house then he may or may not have robbed  previous house.
        #So, maximum loot in that case will be dp[i-1]. Take maximum of both to get maximum loot till current house. 
        dp[i] = max(dp[i-1], dp[i-2] + wealth[i])
    
    #final answer will be stored in dp[n-1]
    return dp[n-1]
    
    
if __name__ == "__main__":
   
    wealth = [int(x) for x in input("Enter the array elements: ").split()]
   
    print(maxLoot(wealth))
