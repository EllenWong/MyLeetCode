'''
806. 写字符串需要的行数
'''
from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        col,row = 0,1
        for i in s:
            col = col + widths[ord(i)-ord('a')]
            if col > 100:
                col = widths[ord(i)-ord('a')]
                row = row + 1
                       
        res = [row,col]
        return res