from functools import cache
from typing import Counter, List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)
        @cache
        # 动态规划
        def dp (mask):
            if mask == 0: return 0
            res = m + 1
            for sticker in stickers:
                left = mask
                cnt = Counter(sticker)
                for i, c in enumerate(target):
                    # print(i,c)
                    if mask >> i & 1 and cnt[c]:
                        cnt[c] -= 1
                        left ^= 1<<i
                if left < mask:
                    res = min(res, dp(left)+1)
            return res

        res = dp( (1<<m) -1 )
        return res if res <= m else -1

stickers = ["with","example","science"]
target = "thehat"
s = Solution()
print(s.minStickers(stickers,target))
