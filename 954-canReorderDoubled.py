'''给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/array-of-doubled-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import *

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # arr.sort(key = abs)
        cnt = Counter(arr) #将数组压缩为哈希表计数
        if cnt[0]%2: return False #对0进行处理
        # print(cnt)
        nn = sorted(cnt,key = abs) #对哈希表进行按绝对值的排序
        # print(nn)
        for num in nn: #对哈希表中的元素进行遍历
            if cnt[num] > cnt[2*num] : return False
            cnt[2*num] -= cnt[num]
        return True