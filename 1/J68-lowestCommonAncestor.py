# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 对二叉搜索树的遍历
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root
        while res:
            if p.val < res.val and q.val < res.val: res = res.left #左子树比当前节点小
            elif p.val > res.val and q.val > res.val: res = res.right #右子树比当前节点大
            else:break
        return res

# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        if root.val == p.val or root.val == q.val: return root #节点值唯一

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return root