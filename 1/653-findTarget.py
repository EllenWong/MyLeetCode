'''
给定一个二叉搜索树 root 和一个目标结果 k,如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

'''

# Definition for a binary tree node.

# encoding: utf-8
import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST: #二叉搜索树的定义
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    # 搜索
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    # 插入
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    # 删除
    def delete(self, root, data):
        flag, n, p = self.search(root, root, data)
        if flag is False:
            print('无该关键字，删除失败')
        else:
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild
                del p
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
                del p
            else:  # 左右子树均不为空
                pre = n.rchild
                if pre.lchild is None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del p


    # 先序遍历
    def preOrderTraverse(self, node):
        if node is not None:
            print(node.data)
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)

    # 中序遍历
    def inOrderTraverse(self, node):
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print(node.data)
            self.inOrderTraverse(node.rchild)

    # 后序遍历
    def postOrderTraverse(self, node):
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print(node.data)

# a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
# bst = BST(a)  # 创建二叉查找树
# bst.inOrderTraverse(bst.root)  # 中序遍历
# bst.delete(bst.root, 49)
# bst.inOrderTraverse(bst.root)

a = [5,3,6,2,4,7]
bst = BST(a)

class Solution:
    def __init__(self):
        self.s = set()
    def dfsfindTarget(self, root: Node, k: int) -> bool: #72ms
        if not root: return False
        if k - root.data in self.s: return True
        self.s.add(root.data)
        return self.dfsfindTarget(root.lchild, k) or self.dfsfindTarget(root.rchild, k)

    def bfsfindTarget(self, root: Node, k: int) -> bool: #68ms
        if not root: return False
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if k - node.data in self.s: return True
            self.s.add(node.data)
            if node.lchild: queue.append(node.lchild)
            if node.rchild: queue.append(node.rchild)
        return False


s = Solution()
k = 9
print(s.bfsfindTarget(bst.root,k))

