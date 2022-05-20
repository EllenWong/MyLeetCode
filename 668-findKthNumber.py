class Solution:
    def cnt(self,mid,m,n):
        ret,i,j = 0,m,1
        while i>=1 and j <= n:
            if i*j <=mid:
                ret += i
                j += 1
            else:
                i -= 1
        return ret
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l,r = 1,m*n
        while l<r:
            mid = (l+r)>>1
            if self.cnt(mid,m,n) < k:
                l = mid + 1
            else:
                r = mid
        return l

s = Solution()
m = 3 
n = 3
k = 5
print(s.findKthNumber(m,n,k))