'''
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        #深度优先搜索
        res = list()
        path = list()
        #用于搜索路径总和等于给定目标的路径
        def dfs(root, target):
            if not root: return 
            path.append(root.val)
            target = target-root.val
            if not root.left and not root.right and target == 0:
                res.append(path[:])
            dfs(root.left,target) 
            dfs(root.right,target)
            path.pop()

        dfs(root,target)
        return res