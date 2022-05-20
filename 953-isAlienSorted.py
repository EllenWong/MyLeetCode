from itertools import pairwise
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {c: i for i, c in enumerate(order)}
        # for word in words:
        #     for s, t in pairwise([c for c in word]):
        #         print(s,t)
        #         print(index[s]<= index[t])
        return all(s <= t for s, t in pairwise([index[c] for c in word] for word in words))

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

s = Solution()
print(s.isAlienSorted(words,order))