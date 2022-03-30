'''输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。'''


import functools
from typing import List

#----------------------内置函数求解问题------------------------------------
#核心排序sort：采用了Timesort算法，是结合归并算法和插入排序的算法，时间复杂度为O(nlogn)，空间复杂度为O(n)
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        #定义排序规则，当x+y > y+x时，返回1，进行排序
        def cmp(x,y):
            if x + y > y + x: return 1
            elif x + y < y + x: return -1
            else:return 0

        s = [str(ss) for ss in nums] #将整数列表转变为字符串列表
        s.sort(key = functools.cmp_to_key(cmp)) #根据自定义规则进行排序
        return ''.join(s)

# Python 定义在函数 sort_rule(x, y) 中；
# Java 定义为 (x, y) -> (x + y).compareTo(y + x) ；
# C++ 定义为 (string& x, string& y){ return x + y < y + x; } ；

#-----------------------快速排序求解问题------------------------------------
class Solution2:
    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(l , r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)
        
        strs = [str(num) for num in nums]
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)

n = [10,2]
s = Solution()
print(s.minNumber(n))