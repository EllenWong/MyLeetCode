'''
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_Maxsum = nums[0]
        pre = 0
        for i in range(len(nums)):
            pre = max(pre+nums[i],nums[i])
            sub_Maxsum = max(sub_Maxsum,pre)

        return sub_Maxsum

s = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(a))