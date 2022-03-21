'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

输入：A = [1,2,3], B = [3,1]
输出：false

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A: return False
        def compare(A,B): #逐一比较A与B
            if not B: return True #B全部匹配完成
            if not A or A.val != B.val: return False #A为空或者AB之间匹配失败
            return compare(A.left,B.left) and compare(A.right,B.right)

        return compare(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)