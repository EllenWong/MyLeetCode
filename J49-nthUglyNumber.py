'''
剑指 Offer 49. 丑数
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        a,b,c = 0,0,0
        for i in range(1,n):
            dp[i] = min(2*dp[a],3*dp[b],5*dp[c])
            if dp[i] == 2*dp[a]: a += 1
            if dp[i] == 3*dp[b]: b += 1
            if dp[i] == 5*dp[c]: c += 1        
        return dp[n-1]