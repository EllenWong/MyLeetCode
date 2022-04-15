'''给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。'''

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        def dfs(i,j,k):
            if not (i>=0 and i<len(board)) or not (j>=0 and j<len(board[0])) or board[i][j]!= word[k] or vis[i][j] ==1:
                return False
            if k == len(word)-1: return True
            vis[i][j] = 1
            res = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            vis[i][j] = 0
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0): return True
        return False

#--------------------------直接在board上修改，将访问到的元素删除--------------------------------
class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False
