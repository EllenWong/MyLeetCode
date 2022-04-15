from typing import List

'''
自除数 是指可以被它包含的每一位数整除的数。

例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
自除数 不允许包含 0 。

给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数 。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/self-dividing-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def judge(n):
            c = 0
            nn = n
            while n:
                m = n % 10
                if m == 0: return False
                if nn % m == 0 and m!=0:
                    c = c + 1
                n //= 10
            if c == len(str(nn)) : return True
            else: return False

        res = []
        for i in range(left,right+1):
            if judge(i) == True:
                print(i)
                res.append(i)
        return res

s = Solution()
print(s.selfDividingNumbers(1,22))