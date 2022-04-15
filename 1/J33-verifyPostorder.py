'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

'''

#方法一：递归分治，时间复杂度O(n^2) 空间复杂度O(N)
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i,j):
            if i>=j: return True
            #划分左右子树，即寻找第一个大于根节点的节点，索引记为m
            p = i
            while postorder[p] < postorder[j]: p = p + 1
            m = p
            while postorder[p] > postorder[j]: p = p + 1
            # 判断此树及此树的左右子树是否正确
            return p == j and recur(i, m-1) and recur(m,j-1)
            
        return recur(0,len(postorder)-1) 

#方法二：辅助单调栈，时间复杂度O(N) 空间复杂度O(N)
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack, root = [], float("+inf") #stack是一个单调栈，存储递增的一个数组
        for i in range(len(postorder) - 1, -1, -1): #从右向左进行遍历
            if postorder[i] > root: return False  #ri（应该在root的左树）大于其父节点，不是二叉搜索树
            while(stack and postorder[i] < stack[-1]): #每当遇到递减的节点，通过出栈来寻找ri的父节点
                root = stack.pop()
            stack.append(postorder[i]) #当前节点入栈
        return True
