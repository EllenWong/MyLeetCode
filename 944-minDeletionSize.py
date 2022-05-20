from itertools import pairwise
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(column) != sorted(column) for column in zip(*strs))


# 关于zip函数：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
strs = ["cba","daf","ghi"]
for column in zip(strs):
    print(column)
# > 返回结果
# ('cba',)
# ('daf',)
# ('ghi',)
for column in zip(*strs):
    print(column)
# > 返回结果
# ('c', 'd', 'g')
# ('b', 'a', 'h')
# ('a', 'f', 'i')
for column in zip(*strs):
    for x, y in pairwise(column):
        print(x,y)
# > pairwise返回结果
# c d
# d g
# b a
# a h
# a f
# f i

class Solution2:
    def minDeletionSize(strs: List[str]) -> int:
        return sum(any(x > y for x, y in pairwise(col)) for col in zip(*strs))  # 空间复杂度为 O(m)，改用下标枚举可以达到 O(1)


s = Solution2
ss = ["cba","daf","ghi"]
print(s.minDeletionSize(strs=ss))