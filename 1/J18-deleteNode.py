'''
定义函数删除链表中的某一个节点
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre,cur = head,head.next #pre和cur分别用来存储当前节点与下一个节点（双指针的做法）

        while cur and cur.val != val:
            pre,cur = cur,cur.next

        if cur: pre.next = cur.next
        return head