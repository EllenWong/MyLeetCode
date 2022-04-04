'''写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。'''
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a,b = a&x,b&x
        while b:
            c = (a & b )<<1 #表示进位的情况
            a = a^b #无进位的加法
            b = c & x #进位
        return a if a <= 0x7fffffff else ~(a ^ x)

s = Solution()
print(s.add(1,2))
