'''
输入: "the sky is blue"
输出: "blue is sky the"
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s)-1 #i和j分别代表从右到左的所有单词的左右的index
        res = []
        while i>=0:
            while i>=0 and s[i]!=' ':
                i = i - 1
            res.append(s[i+1:j+1])
            while s[i] == ' ':
                i = i - 1
            j = i
        return ' '.join(res) #用空格间断所有res的值
            