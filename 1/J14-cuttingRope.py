class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        for i in range(3,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],max((i-j)*j,dp[i-j]*j))
        return dp[n]