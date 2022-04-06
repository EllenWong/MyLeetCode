'''最小高度树'''
from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        g = [[] for _ in range(n)]
        for x,y in edges: #存储该无向图
            g[x].append(y)
            g[y].append(x)
        parent = [0]*n #定义当前节点的父节点

        def bfs(start:int):
            vis = [False] * n
            vis[start] = [True] #start节点已访问
            q = deque([start])
            while q:
                x = q.popleft() # x出队
                for y in g[x]: #对所有与x相邻的节点遍历
                    if not vis[y]:
                        vis[y] = True #更高当前访问情况
                        parent[y] = x
                        q.append(y)
            return x
        
        x=bfs(0) #与0最远的节点
        y=bfs(x) #与x最远的节点
        parent[x] = -1

        path = [] #存储最长路径的相应节点
        while y!=-1:
            path.append(y)
            y = parent[y]
        m = len(path)
        return [path[m//2]] if m % 2 else [path[m//2-1],path[m//2]]

class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        g = [[] for _ in range(n)]
        for x,y in edges: #存储该无向图
            g[x].append(y)
            g[y].append(x)
        parent = [0]*n #定义当前节点的父节点

        maxDepth, node = 0,-1

        def dfs(x:int,pa:int,depth:int):
            nonlocal maxDepth, node
            if depth > maxDepth: #更新当前最长路径与当前节点
                maxDepth,node = depth,x 
            parent[x] = pa #更新当前节点的父节点
            for y in g[x]: #对所有不是x的父节点且与x相邻的节点遍历
                if y!=pa:
                    dfs(y,x,depth+1)
        dfs(0,-1,1)
        maxDepth = 0
        dfs(node,-1,1) #node即与0最远的节点

        path = [] #存储最长路径的相应节点
        while node!=-1:
            path.append(node)
            node = parent[node]
        m = len(path)
        return [path[m//2]] if m % 2 else [path[m//2-1],path[m//2]]

n = 4
edges = [[1,0],[1,2],[1,3]]
s = Solution2()
print(s.findMinHeightTrees(n,edges))


