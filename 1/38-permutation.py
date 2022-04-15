from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(le): #递归的方式，le表示当前访问的字母index
            if le == len(c)-1: #全部访问完成
                res.append(''.join(c))
                return
            dic = set() #定义集合判断当前元素是否已经被访问
            for i in range(le,len(c)):
                if c[i] in dic: continue #当前元素已经在集合中
                dic.add(c[i])
                c[i], c[le] = c[le], c[i]
                dfs(le+1)
                c[i], c[le] = c[le], c[i]
        dfs(0)
        return res