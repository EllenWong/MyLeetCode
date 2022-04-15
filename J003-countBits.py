class Solution:
    def countBits(self, n: int) -> List[int]:
        bit = [0]
        for i in range(1,n+1):
            bit.append(bit[i>>1]+(i&1))
        return bit