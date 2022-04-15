'''
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
'''

# Definition for a binary tree node.
from turtle import right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def compare(L,R): #对左右子树的比较
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return compare(L.left,R.right) and compare(L.right,R.left)

        return compare(root.left,root.right)
