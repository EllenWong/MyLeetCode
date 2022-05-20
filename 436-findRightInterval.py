from tkinter import N
from turtle import st
from typing import List
from xml.dom.minicompat import EmptyNodeList


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = [-1] * len(intervals)
        # 将原list中的start 和 end拆分开
        starts, ends = list(zip(*intervals))
        # 对start 和 end 排序
        starts = sorted(zip(starts,range(len(intervals))))
        ends = sorted(zip(ends,range(len(intervals))))
        # print(starts)
        # print(ends)

        j = 0
        for end, id in ends:
            while j < len(intervals) and starts[j][0] < end:
                j += 1
            if j < len(intervals):
                res[id] = starts[j][1]
        return res

intervals = [[3,4],[2,3],[1,2]]
s = Solution()
print(s.findRightInterval(intervals))