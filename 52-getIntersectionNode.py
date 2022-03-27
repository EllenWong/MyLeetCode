'''两个列表的第一个公共节点'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #返回值为某一个节点
        nodeA,nodeB = headA,headB
        while nodeA != nodeB:
            if nodeA!=None:
                nodeA = nodeA.next
            else:
                nodeA = headB
            if nodeB!=None:
                nodeB = nodeB.next
            else:
                nodeB = headA
        return nodeA