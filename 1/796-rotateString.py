class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def roate(s:str):
            res = s[1:]
            res += s[0]
            return res
        r = s
        for i in range(len(s)):
            r = roate(r)
            if r == goal:
                return True
        return False