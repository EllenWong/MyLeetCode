'''
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
'''

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归的方式
    def mirrorTree(self, root: TreeNode) -> TreeNode: #36ms
        if not root: return None
        tmp = root.left
        root.left = self.mirrorTree(root.right) 
        root.right = self.mirrorTree(tmp)
        return root

    #非递归的方式
    def mirrorTree(self, root: TreeNode) -> TreeNode: #36ms
        if not root: return None
        stack = []
        stack.append(root) #用栈的方式对节点进行存储
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left,node.right = node.right,node.left
        return root
