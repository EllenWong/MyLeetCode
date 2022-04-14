class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1,0 #位因子与统计结果
        high, cur, low = n//10, n%10, 0
        while high!=0 or cur!=0:
            #根据当前位分类讨论，计算当前位出现1的个数
            if cur == 0:
                res += high*digit
            elif cur == 1:
                res += high*digit + low + 1
            else: 
                res += (high+1)* digit
            #更新下一轮循环
            low = low + cur*digit 
            cur = high % 10
            high = high // 10
            digit = digit * 10 
        return res