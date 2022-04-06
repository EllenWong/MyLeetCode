'''数组中出现次数超过一半的数字'''
from typing import Counter, List

# 方法一：哈希表的解法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max(cnt.keys(),key = cnt.get)

# 方法二：摩尔投票法
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        for num in nums:
            if vote == 0: x = num
            if num == x: vote += 1
            if num != x: vote -= 1
        return x