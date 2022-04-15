class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<4: return n-1
        res = 1 #最终结果
        while n > 4:
            res *= 3 % 1000000007
            n -= 3
        return res * n % 1000000007