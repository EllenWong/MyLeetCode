'''
请实现一个函数，把字符串 s 中的每个空格替换成"%20".

示例 1:

输入: s = "We are happy."
输出："We%20are%20happy."

'''


class Solution:
    def replaceSpace(self, s: str) -> str:
        l = len(s)
        res = []
        for i in range(l):
            c = s[i]
            if c == ' ':
                res.append("%20")
            else:
                res.append(c)
        return "".join(res)

s = "We are happy."
c = Solution()
print(c.replaceSpace(s))