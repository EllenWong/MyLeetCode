'''在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。'''
from typing import List

# 有限状态自动机
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones,twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones