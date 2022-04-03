'''快速幂的方法'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: 
            x, n = 1 / x, -n
        while n:
            if n & 1: res *= x #当n是奇数的情况
            x *= x
            n >>= 1
        return res