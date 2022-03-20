'''
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
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
        res = []
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        while queue:
            ll = []
            for _ in range(len(queue)): #对每一层进行遍历
                node = queue.popleft()
                ll.append(node.val)
                if node.left: queue.append(node.left) #引入左右节点
                if node.right: queue.append(node.right)
            res.append(ll)
        return res