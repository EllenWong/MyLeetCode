'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def translateNum(self, num: int) -> int:
        nu = list(str(num))
        for i in range(len(nu)):
            nu[i] = int(nu[i]) #将整数转变为列表的形式存储

        s = [0 for i in range(len(nu))] #动态规划初始化
        s[0] = 1
        if len(nu)<2: return 1
        if nu[0] * 10 + nu[1] > 25 : s[1] = 1 
        else: s[1] = 2

        for i in range(2,len(nu)): #动态规划动态转移
            if nu[i] + nu[i-1]*10 > 25 or nu[i-1]==0: s[i] = s[i-1]
            else: s[i] = s[i-1] + s[i-2]
        return s[-1]
    
n = 1
s = Solution()
print(s.translateNum(n))
