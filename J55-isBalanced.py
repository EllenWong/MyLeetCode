#平衡二叉树，每一个节点的左右子节点深度不大于1
# Definition for a binary tree node.
from turtle import right
from torch import le


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#方法一：先序遍历+判断深度 时间复杂度O(nlogn) 空间复杂度O(n)
class Solution: 
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None: return True
        def maxdepth(root):
            if root == None: return 0
            return max(maxdepth(root.left)+1, maxdepth(root.right)+1)
        cmp = maxdepth(root.left) - maxdepth(root.right)
        if  cmp > 1 or cmp < -1: return False 
        return self.isBalanced(root.left) and self.isBalanced(root.right)

#方法二：后序遍历+剪枝 时间复杂度O(n) 空间复杂度O(n)
class Solution: 
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if root == None: return 0
            left = recur(root.left) #递归左子树
            if left == -1: return -1 #说明左子树不是平衡树
            right = recur(root.right) #递归右子树
            if right == -1: return -1 #说明右子树不是平衡树
            return max(left,right) +1 if abs(left - right) <=1 else -1 
        return recur(root) != -1