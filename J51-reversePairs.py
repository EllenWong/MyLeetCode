class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r): #归并排序
            # 终止条件
            if l >= r: return 0 #当分组中只剩一个元素时
            # 递归划分
            m = (l + r) // 2 
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1] #暂存辅助数组
            for k in range(l, r + 1): 
                if i == m + 1:  #说明左子数组已经合并完
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]: #说明右子数组已经合并完
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j] # 出现逆序对
                    j += 1
                    res += m - i + 1 # 统计逆序对
            return res
        
        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)