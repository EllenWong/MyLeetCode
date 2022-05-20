from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        for num in nums:
            ret += abs(num - nums[len(nums)//2])
        return ret
