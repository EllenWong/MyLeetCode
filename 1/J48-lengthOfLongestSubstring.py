'''
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''
#-------------------哈希表与双指针------------------------
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic,i,j = {},-1,0
        res = 0
        for j in range(len(s)):
            if s[j] in dic:
                i = max(i,dic[s[j]]) #更新左指针
            dic[s[j]] = j
            res = max(res,j-i) #更新结果
        return res     