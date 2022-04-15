'''
统计一个数字在排序数组中出现的次数。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

'''

#二分法求解问题--分别求有序数组的上下边界
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] <=target:
                l = mid + 1
            else:
                r = mid - 1
        right = l
        if r>=0 and nums[r] !=target:
            return 0 
        l = 0
        while l<=r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        left = r
        return right-left-1
