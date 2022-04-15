
from typing import List

##---------------直接遍历-------------------
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tot, num = 0, 0
                for x in range(max(i - 1, 0), min(i + 2, m)): #利用双重循环对过滤器中的元素进行均值的计算。
                    for y in range(max(j - 1, 0), min(j + 2, n)):
                        tot += img[x][y]
                        num += 1
                ans[i][j] = tot // num
        return ans

img = [[1,1,1],[1,0,1],[1,1,1]]
s = Solution()
print(s.imageSmoother(img))