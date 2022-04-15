#-------二叉树的深度-----------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: #深度优先搜索
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        return max( self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)

class Solution2: #广度优先搜索
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue: #将当前节点的左右自节点加入到队列中
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1 #遍历完每一层时，深度+1
        return res