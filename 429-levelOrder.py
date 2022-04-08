'''429. N 叉树的层序遍历'''

from collections import deque
from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        ans = []
        q = deque([root])
        while q:#典型的层序遍历题目
            cnt = len(q) #当前层的节点数
            level = [] #存储当前层的节点
            for _ in range(cnt): 
                cur = q.popleft()
                level.append(cur.val)
                for child in cur.children:
                    q.append(child)
            ans.append(level)
        return ans