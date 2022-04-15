from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i,j = 1,1
        res = []
        su = 0
        while i <= target // 2:
            if su < target:
                su += j
                j += 1
            elif su > target:
                su -= i
                i += 1
            else:
                lis = list(range(i,j))
                res.append(lis)
                su -= i
                i += 1
        return res
