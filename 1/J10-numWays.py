'''
一只青蛙一次可以跳上1级台阶,也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
'''

class Solution:
    def numWays(self, n: int) -> int:
        res = [1,1,2]
        for i in range(3,n+1):
            res.append((res[i-1]+res[i-2])%1000000007)
        return res[n]