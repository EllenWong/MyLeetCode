'''输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#方法一：递归
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left:int, preorder_right:int, inorder_left:int, inorder_right:int):
            if preorder_left > preorder_right: return None

            #对先序遍历和中序遍历的根节点赋值,并建立根节点
            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_left]]
            root = TreeNode(preorder[preorder_left])

            #对接下来要遍历的左右子树进行定位
            size_left = inorder_root - inorder_left
            root.left = myBuildTree(preorder_left + 1,preorder_left + size_left, inorder_left, inorder_root-1)
            root.right = myBuildTree(preorder_left + size_left+1,preorder_right,inorder_root+1,inorder_right)
            return root

        n = len(preorder)
        # 构造哈希表，快速寻找根节点
        index = {element: i for i,element in enumerate(inorder)}
        return myBuildTree(0,n-1,0,n-1)

# 方法二：迭代法
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)

        return root