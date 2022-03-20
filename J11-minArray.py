'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
'''

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        for i in range(len(numbers)-1):
            if numbers[i]>numbers[i+1]:
                return numbers[i+1]
        return numbers[0]

#用二分法进行问题求解
# class Solution:
#     def minArray(self, numbers: List[int]) -> int:
#         low, high = 0, len(numbers) - 1
#         while low < high:
#             pivot = low + (high - low) // 2
#             if numbers[pivot] < numbers[high]:
#                 high = pivot 
#             elif numbers[pivot] > numbers[high]:
#                 low = pivot + 1
#             else:
#                 high -= 1
#         return numbers[low]
