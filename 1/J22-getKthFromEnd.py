# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        pre,cur = head,head
        c = 0
        while cur:
            c = c + 1
            cur = cur.next
        while c-k:
            pre = pre.next
            c = c - 1
        return pre