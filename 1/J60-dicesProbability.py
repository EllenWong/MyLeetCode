'''
剑指 Offer 60. n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
'''
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1/6]*6
        for i in range(2,n+1):
            tmp = [0] * (5*i+1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j+k] += dp[j] / 6
            dp = tmp
        return dp