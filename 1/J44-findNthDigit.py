class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1,1,9 #表示当前位数，起始数字与数位数量
        # 计算所求数位所在的数字位数
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        # 确定所求数位所在的数字
        num = start + (n-1) // digit
        # 确定所求数位在num的哪一数位
        s = str(num)
        res = int(s[(n-1)%digit])
        return res