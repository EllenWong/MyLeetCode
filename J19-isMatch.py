'''
剑指 Offer 19. 正则表达式匹配
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls,lp = len(s)+1,len(p)+1
        dp = [[False]*lp for _ in range(ls)]
        dp[0][0] = True
        for j in range(2,lp,2):#只有偶数位都为*时，才能进行匹配
            dp[0][j] = dp[0][j-2] and p[j-1] == '*'
        for i in range(1,ls):
            for j in range(1,lp):
                if p[j-1] == '*':
                    if dp[i][j-2]: dp[i][j] = True
                    elif dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'):
                        dp[i][j] = True
                else:
                    if dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.'): 
                        dp[i][j] =True

        return dp[ls-1][lp-1]