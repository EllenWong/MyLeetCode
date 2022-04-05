import functools
from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x,y : x^y,nums) #也就是a与b异或的结果
        a,b = 0,0
        div = 1
        while div & ret == 0: #找到a与b不同的某一位，即异或结果为1
            div <<= 1
        for num in nums: #对nums中的所有元素进行分组处理
            if num & div: # 与a为同一组的元素
                a^=num #消掉除了a以外的元素
            else: # 与b为同一组的元素
                b^=num #消掉除了b以外的元素
        return a,b
