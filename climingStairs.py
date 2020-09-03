__author__ = 'Jie'
"""
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        DP, bottom-up
        :param n: the number of stairs
        :return:
        """
        myList=[0 for i in range(n+2)]
        myList[0]=0
        myList[1]=1
        for i in range(2,n+2):
            myList[i]=myList[i-1]+myList[i-2]
        return myList[n+1]

    def climbStairs_re(self,n):
        if n<=2:
            return n
        return self.climbStairs_re(n-1)+self.climbStairs_re(n-2)

solution=Solution()
result=solution.climbStairs(8)
print (result)