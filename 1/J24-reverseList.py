'''
剑指Offer 24. 反转链表

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

限制：

0 <= 节点个数 <= 5000

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None #要返回的节点
        cur = head #当前节点
        while cur: #没有完全遍历完所有节点时
            tmp = cur.next #存储下一个节点
            cur.next = pre #反转
            pre = cur #修改反转后的链表
            cur = tmp #访问下一个节点
        return pre


        