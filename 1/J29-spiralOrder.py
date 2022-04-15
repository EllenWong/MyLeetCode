'''剑指 Offer 29. 顺时针打印矩阵'''
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []

        row, column = len(matrix), len(matrix[0])
        # vis = [[0 for _ in range(column)] for _ in range(row)]
        res = []
        l ,r ,t,b= 0,column,0,row
        while l<=r-1 and t<=b-1:
            for cc in range(l,r):
                res.append(matrix[t][cc])
            for rr in range(t+1,b):
                res.append(matrix[rr][r-1])
            if l<r-1 and t<b-1:
                for cc in range(r-2,l,-1):
                    res.append(matrix[b-1][cc])
                for rr in range(b-1,t,-1):
                    res.append(matrix[rr][l])
            l,r,t,b = l+1,r-1,t+1,b-1
        return res
            
                