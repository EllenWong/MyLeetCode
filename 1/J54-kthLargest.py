'''
给定一棵二叉搜索树，请找出其中第 k 大的节点的值。

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            #二叉搜索树中序遍历得到从小到大的元素

            dfs(root.right) #遍历右节点
            # if self.curnode == 0:return
            self.curnode = self.curnode - 1 #更新当前访问的数值
            if self.curnode == 0: 
                self.res = root.val
                return 
            dfs(root.left) #遍历左节点

        self.curnode = k
        dfs(root)
        return self.res