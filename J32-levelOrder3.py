'''
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
'''

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        res = []
        queue = collections.deque()
        queue.append(root)
        flag = 1
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right:queue.append(node.right)
            if flag%2:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            flag += 1
        return res

# [1]
# [2,3]
# [3,4,5]
# [4,5,6,7]