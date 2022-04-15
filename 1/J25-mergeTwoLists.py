'''合并两个链表'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0) #初始化第一个节点为0，最后删掉。
        cur = res
        while l1 and l2:
            if l1.val < l2.val: #对下一个节点的赋值！！！cur相当于一个关于res的指针。
                cur.next,l1 = l1,l1.next 
            else:
                cur.next,l2 = l2,l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return res.next 