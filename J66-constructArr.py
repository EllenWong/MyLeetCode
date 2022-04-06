'''构建乘积数组'''
from typing import List
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        tmp = 1
        b = [1]*len(a)
        # 下三角矩阵的计算（前缀积）
        for i in range(1,len(a)):
            b[i] = b[i-1] * a[i-1]
        # 上三角矩阵的计算（后缀积）
        for i in range(len(a)-2,-1,-1):
            tmp = tmp * a[i+1]        
            b[i] = b[i] * tmp
        return b