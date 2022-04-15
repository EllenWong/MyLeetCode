'''
将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
'''

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        #循环双向链表，左前驱，右后继
        if not root: return
        def dfs(root):
            if not root:return
            dfs(root.left)

            #对二叉搜索树进行中序遍历
            if self.pre:
                self.pre.right = root #后继
                root.left = self.pre #前驱
            else:
                self.head = root #前驱节点不存在时，修改当前节点为头节点
            self.pre = root #存储pre作为前驱节点

            dfs(root.right)
        
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre,self.head
        return self.head