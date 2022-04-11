class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        #总共9个样例，组合数
        if n == 0: return 1
        if n == 1: return 10
        res, cur = 10, 9
        for i in range(n-1):
            cur *= 9-i
            res += cur
        return res