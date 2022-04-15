'''
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：

如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 方法一：线性查找

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i>target:
                return i
        return letters[0]

# 方法二：二分查找
class Solution2:
    def nextGreatestLetter(self, letters:List[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n-1
        while l != r:
            mid = (l+r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        if l == n-1 and letters[l] <= target:
            return letters[0]
        return letters[l]

lis = [1,2,3,4,5]
t = 3
s = Solution2()
print(s.nextGreatestLetter(lis,t))
