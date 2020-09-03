__author__ = 'Jie'
"""
322. Coin Change
Medium

You are given coins of different denominations and a
total amount of money amount. Write a function to compute the fewest number of coins
that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""
import math

class Solution:
    def coinChange_dp(self, coins, amount) -> int:
        """
        DP: bottom-up
        :param coins: denominations of different coins; List[int]
        :param amount: overall amount; int
        :return: the minimum number of coins used.
        """
        minNum=[0]+[-1]*amount
        for money in range(1,amount+1):
            minNum[money]=math.inf
            for coin in coins:
                if money>=coin:
                    numCoins=minNum[money-coin]+1
                    if numCoins<minNum[money]:
                        minNum[money]=numCoins

        if minNum[amount]==math.inf:
            return -1
        return minNum[amount]


    def help_re(self, coins, amount):
        """
        recursive algorithm
        """
        if amount ==0:
            return 0
        minNum=math.inf
        for coin in coins:
            if amount>=coin:
                numCoins=self.help_re(coins,amount-coin)
                if numCoins<minNum:
                    minNum=numCoins+1
            # return -1
        return minNum

    def coinChange_re(self,coins,amount):
        minNum=self.help_re(coins,amount)
        return minNum if minNum!=math.inf else -1

solution=Solution()
coins = [1, 2, 5]
amount = 11
# coins = [2]
# amount = 3
minNum=solution.coinChange_re(coins,amount)
print (minNum)
