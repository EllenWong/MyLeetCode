'''
剑指 Offer 06. 从尾到头打印链表

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1:

输入: head = [1,3,2]
输出：[2,3,1]


限制：

0 <= 链表长度 <= 10000

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        stack = [] 
        while head:
            stack.append(head.val) #从头部节点一一入栈
            head = head.next #遍历下一个元素

        return stack[::-1] #倒序输出stack的值

# class Solution: #采用递归的方式进行求解
#     def reversePrint(self, head: ListNode) -> list[int]:
#         return self.reversePrint(head.next) + [head.val] if head else []

   