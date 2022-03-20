'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
'''

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #使用队列完成广度优先遍历BFS，先入先出
    def levelOrder(self, root: TreeNode) -> list[int]:
        if not root: return []
        res = []
        queue = collections.deque() #队列定义方式
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
            res.append(node.val)

        return res

#python中collections的用法
#from collecttions import xxx
#1. namedtuple：创建元组对象并规定元素个数，用属性来引用tuple的某个元素
#2. deque：队列，实现了插入和删除的双向列表
#3. defaultdict：当key不存在时，返回一个默认值
#4. orderedDict：按照插入的顺序来保持key的顺序
#5. counter：简单的计数器，如，统计字符出现的个数